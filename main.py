#!/usr/bin/env python
"""
AI Debugging Assistant - Main Entry Point

Exposes the FastAPI `app` object so Vercel's Python runtime can detect it.
Run locally with:
    python main.py
"""

import os
import sys

# Ensure project root is on the path (needed for relative imports when Vercel
# invokes this file directly from the project root)
sys.path.insert(0, os.path.dirname(__file__))

from apps.debugging_assistant.app import app  # noqa: F401  ← Vercel detects this

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    print(f"[*] Starting AI Debugging Assistant on http://localhost:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
