"""
Vercel entrypoint — api/index.py

Vercel's Python runtime auto-detects `app` in files under api/.
All requests are routed here via vercel.json, and FastAPI handles
the internal routing (/, /api/debug, /api/generate-code, /health).
"""

import sys
import os

# Add project root to path so imports like `apps.*` and `utils.*` resolve
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from apps.debugging_assistant.app import app  # noqa: F401 — Vercel detects this
