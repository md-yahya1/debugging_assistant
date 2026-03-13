"""
Main entry point for Streamlit Cloud deployment.
Delegates to the debugging assistant application.
"""
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import and run the main app
from apps.debugging_assistant.app import main

if __name__ == "__main__":
    main()
