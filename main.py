#!/usr/bin/env python
"""
AI Debugging Assistant - Main Entry Point

Run the debugging assistant with:
    python main.py
"""

import subprocess
import sys
import os

def main():
    """Start the FastAPI server for the debugging assistant"""
    try:
        print("[*] Starting AI Debugging Assistant...")
        port = int(os.environ.get("PORT", 8000))
        print(f"[*] Server will be available at: http://localhost:{port}")

        # Run the FastAPI app
        from apps.debugging_assistant.app import app
        import uvicorn

        uvicorn.run(app, host="0.0.0.0", port=port)
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
