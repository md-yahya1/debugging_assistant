"""
api/index.py — Vercel serverless entrypoint for AI Debugging Assistant

This file is self-contained so Vercel's Python runtime can detect `app = FastAPI()`
without relying on sys.path manipulation or cross-directory relative imports.
All application logic is inlined here.

Local development: run `python main.py` from the project root instead.
"""

from __future__ import annotations

import os
import json
import yaml
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from huggingface_hub import InferenceClient
from pydantic import BaseModel, Field

load_dotenv()

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

class ModelConfig(BaseModel):
    provider: str = Field(default="huggingface")
    name: str = Field(default="Qwen/Qwen2.5-Coder-32B-Instruct")
    temperature: float = Field(default=0.4, ge=0.0, le=1.0)
    top_p: float = Field(default=0.9, ge=0.0, le=1.0)
    max_output_tokens: int = Field(default=2048, ge=1)

class DebuggingAppConfig(BaseModel):
    explanation_language: str = "en"
    max_code_chars: int = 4000

class AppConfig(BaseModel):
    model: ModelConfig = ModelConfig()
    debugging_app: DebuggingAppConfig = DebuggingAppConfig()


def _load_config() -> AppConfig:
    # Path resolves relative to this file: api/ → project root → config/config.yaml
    config_path = Path(__file__).resolve().parent.parent / "config" / "config.yaml"
    if config_path.exists():
        with config_path.open("r", encoding="utf-8") as f:
            raw = yaml.safe_load(f) or {}
        return AppConfig(**raw)
    return AppConfig()  # fall back to defaults if config is missing


_config = _load_config()

# ---------------------------------------------------------------------------
# LLM Client
# ---------------------------------------------------------------------------

class HuggingFaceClient:
    def __init__(self, api_key: Optional[str] = None):
        self.model_cfg = _config.model
        self.api_key = api_key or os.getenv("HF_API_KEY")
        if not self.api_key:
            raise ValueError("HF_API_KEY environment variable is not set.")
        self.client = InferenceClient(model=self.model_cfg.name, token=self.api_key)

    def ask(self, prompt: str) -> str:
        default_system = "You are a helpful and concise assistant. Answer efficiently."
        if any(kw in prompt for kw in ("You are an AI Debugging Assistant",
                                        "Beginner-Friendly Explanation",
                                        "user has provided the following code")):
            messages = [{"role": "user", "content": prompt}]
        else:
            messages = [
                {"role": "system", "content": default_system},
                {"role": "user", "content": prompt},
            ]

        response = self.client.chat_completion(
            messages=messages,
            max_tokens=self.model_cfg.max_output_tokens,
            temperature=self.model_cfg.temperature,
            top_p=self.model_cfg.top_p,
        )

        try:
            return response.choices[0].message["content"]
        except Exception:
            if isinstance(response, dict):
                if "choices" in response and response["choices"]:
                    first = response["choices"][0]
                    if isinstance(first, dict):
                        if "message" in first and "content" in first["message"]:
                            return first["message"]["content"]
                        if "text" in first:
                            return first["text"]
                if "generated_text" in response:
                    return response["generated_text"]
            if hasattr(response, "generated_text"):
                return response.generated_text
            return str(response)

# ---------------------------------------------------------------------------
# Prompt builders
# ---------------------------------------------------------------------------

def _build_debugging_prompt(user_input: str, language: str = "auto") -> str:
    prompt_path = (
        Path(__file__).resolve().parent.parent
        / "utils" / "prompts" / "debugging_prompt.json"
    )
    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt_json = json.load(f)

    lang_ctx = (
        f"Language Context: {language}\n\n"
        if language and language != "auto"
        else "Language Context: auto-detect\n\n"
    )
    return (
        prompt_json["system_instruction"] + "\n\n"
        + lang_ctx
        + prompt_json["user_prompt_template"].replace("{{USER_INPUT}}", user_input.strip())
    )


def _build_code_gen_prompt(user_request: str, language: str = "python") -> str:
    system = (
        f"You are an expert code generation AI assistant powered by Qwen Coder. "
        f"Generate clean, efficient, and well-commented {language} code based on user requests. "
        f"Follow best practices and include docstrings where appropriate."
    )
    template = (
        f"Generate {language} code for the following task:\n\n"
        f"{user_request.strip()}\n\n"
        f"Requirements:\n"
        f"- Provide working, production-ready code\n"
        f"- Include docstrings and comments\n"
        f"- Handle edge cases\n"
        f"- Use clear variable names\n"
        f"- Follow {language} best practices\n\n"
        f"Code:"
    )
    return system + "\n\n" + template

# ---------------------------------------------------------------------------
# FastAPI app  ← Vercel detects this
# ---------------------------------------------------------------------------

app = FastAPI(title="AI Debugging Assistant")

# Mount static files (works locally; on Vercel, /static/* is served via CDN)
_static_dir = Path(__file__).resolve().parent.parent / "apps" / "debugging_assistant" / "static"
if _static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(_static_dir)), name="static")


class DebugRequest(BaseModel):
    code: str
    language: str = "auto"


class CodeGenerationRequest(BaseModel):
    request: str
    language: str = "python"


@app.get("/", response_class=HTMLResponse)
async def get_home():
    """Serve the main HTML page."""
    html_file = _static_dir / "index.html"
    if html_file.exists():
        return html_file.read_text(encoding="utf-8")
    return "<h1>AI Debugging Assistant</h1><p>Static files not found.</p>"


@app.post("/api/debug")
async def debug_code(request: DebugRequest):
    """Debug the provided code or error log."""
    if not request.code.strip():
        raise HTTPException(status_code=400, detail="Please enter your code or error log.")
    try:
        prompt = _build_debugging_prompt(request.code, request.language)
        result = HuggingFaceClient().ask(prompt)
        return {"success": True, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/generate-code")
async def generate_code(request: CodeGenerationRequest):
    """Generate code from a natural language request."""
    if not request.request.strip():
        raise HTTPException(status_code=400, detail="Please enter a code generation request.")
    try:
        prompt = _build_code_gen_prompt(request.request, request.language)
        result = HuggingFaceClient().ask(prompt)
        return {"success": True, "result": result, "language": request.language}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}
