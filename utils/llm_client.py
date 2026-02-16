from __future__ import annotations
import os
from typing import Optional
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from config.model_config import load_config

load_dotenv()

class HuggingFaceClient:
    def __init__(
        self,
        api_key: Optional[str] = None,
        config_path: Optional[str] = None,
    ):
        self.app_config = load_config(config_path)
        self.model_cfg = self.app_config.model

        self.api_key = api_key or os.getenv("HF_API_KEY")
        if not self.api_key:
            raise ValueError("HF_API_KEY not found.")

        self.client = InferenceClient(
            model=self.model_cfg.name,
            token=self.api_key
        )

    def ask(self, prompt: str) -> str:
        # If the prompt already contains explicit system-level instructions (our
        # debugging prompt includes a system instruction), send it as a single
        # user message so the model sees the instructions verbatim. Otherwise,
        # include a concise default system message.
        default_system = "You are a helpful and concise assistant. Answer efficiently."

        if (
            any(keyword in prompt for keyword in ("You are an AI Debugging Assistant", "Beginner-Friendly Explanation", "user has provided the following code"))
        ):
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

        # The HF InferenceClient may return different shapes depending on model
        # and client version. Try common access patterns and handle both
        # attribute-like objects and plain dict responses.
        try:
            return response.choices[0].message["content"]
        except Exception:
            # dict-like responses
            if isinstance(response, dict):
                # common chat completion shape
                if "choices" in response and response["choices"]:
                    first = response["choices"][0]
                    if isinstance(first, dict):
                        # nested message content
                        if "message" in first and isinstance(first["message"], dict) and "content" in first["message"]:
                            return first["message"]["content"]
                        # some APIs return 'text' or 'output'
                        if "text" in first:
                            return first["text"]
                # top-level generated text
                if "generated_text" in response:
                    return response["generated_text"]
                if "output" in response:
                    return response["output"]

            # object-like responses
            if hasattr(response, "generated_text"):
                return getattr(response, "generated_text")
            if hasattr(response, "text"):
                return getattr(response, "text")

            # Final fallback: stringify the response object
            return str(response)
