import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from utils.llm_client import HuggingFaceClient
from utils.debugging_helper import build_debugging_prompt
from utils.code_generator_helper import build_code_generation_prompt

app = FastAPI(title="AI Debugging Assistant")

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

class DebugRequest(BaseModel):
    code: str

class CodeGenerationRequest(BaseModel):
    request: str
    language: str = "python"

@app.get("/", response_class=HTMLResponse)
async def get_home():
    """Serve the main HTML page"""
    html_file = os.path.join(static_dir, "index.html")
    if os.path.exists(html_file):
        with open(html_file, 'r', encoding='utf-8') as f:
            return f.read()
    return "<h1>Debugging Assistant</h1>"

@app.post("/api/debug")
async def debug_code(request: DebugRequest):
    """Debug the provided code or error log"""
    if not request.code.strip():
        raise HTTPException(status_code=400, detail="Please enter your code or error log")

    try:
        prompt = build_debugging_prompt(request.code)
        client = HuggingFaceClient()
        response = client.ask(prompt)
        return {"success": True, "result": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.post("/api/generate-code")
async def generate_code(request: CodeGenerationRequest):
    """Generate code based on user request using Deepseek Coder"""
    if not request.request.strip():
        raise HTTPException(status_code=400, detail="Please enter your code generation request")

    try:
        prompt = build_code_generation_prompt(request.request, request.language)
        client = HuggingFaceClient()
        response = client.ask(prompt)
        return {"success": True, "result": response, "language": request.language}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)