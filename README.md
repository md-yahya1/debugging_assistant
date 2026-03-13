# AI Debugging Assistant 👨‍🏫

A Streamlit-based AI debugging assistant that helps you analyze and debug your code using cutting-edge language models. Simply describe your coding issue or paste your error log, and get intelligent debugging suggestions.

## Features

- 🤖 **AI-Powered Analysis**: Uses Hugging Face language models for intelligent code debugging
- 💬 **User-Friendly Interface**: Built with Streamlit for an intuitive web UI
- 🔧 **Easy Configuration**: YAML-based configuration for model settings
- 🐳 **Docker Ready**: Includes Dockerfile for containerized deployment
- ⚡ **Fast Processing**: Optimized for quick debugging assistance

## Prerequisites

- Python 3.9+
- Hugging Face API Key (get it free from [Hugging Face](https://huggingface.co/settings/tokens))
- pip or conda for package management

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/md-yahya1/debugging_assistant.git
   cd debugging_assistant
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv

   # On Windows
   .venv\Scripts\activate

   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```

   Edit `.env` and add your Hugging Face API key:
   ```
   HF_API_KEY=your_actual_api_key_here
   ```

## Quick Start

### Running Locally

```bash
streamlit run apps/debugging_assistant/app.py
```

The app will be available at `http://localhost:8501`

### Using Docker

```bash
docker build -t debugging-assistant .
docker run -p 8501:8501 --env-file .env debugging-assistant
```

Access the app at `http://localhost:8501`

## Usage

1. Open the application in your browser
2. Paste your code snippet or error message in the text area
3. Click "🔍 Debug code" to get AI-powered debugging suggestions
4. Review the analysis and apply the recommendations

## Project Structure

```
debugging_assistant/
├── apps/
│   └── debugging_assistant/
│       ├── app.py              # Main Streamlit application
│       └── prompts.py          # Prompt configurations
├── config/
│   ├── config.yaml            # Model and app configurations
│   └── model_config.py         # Python config module
├── utils/
│   ├── debugging_helper.py     # Core debugging logic
│   ├── llm_client.py          # LLM API client
│   ├── text_helpers.py        # Text utilities
│   └── prompts/               # Prompt templates
├── requirements.txt            # Python dependencies
├── Dockerfile                 # Docker configuration
└── README.md                  # This file
```

## Configuration

Edit `config/config.yaml` to customize:
- Model provider and name
- Temperature and probability settings
- Maximum output token length
- Explanation language
- Code character limits for safety

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `HF_API_KEY` | Your Hugging Face API token | Yes |

## Security Notes

⚠️ **Never commit `.env` file to version control!**
- The `.env` file is already added to `.gitignore`
- Use `.env.example` as a template for other developers
- Keep your API keys private and secure

## Troubleshooting

**Issue**: `FileNotFoundError: Debugging prompt file not found`
- Solution: Ensure you're running from the project root directory

**Issue**: `HFValidationError: Could not connect to Hugging Face`
- Solution: Verify your `HF_API_KEY` is valid and has appropriate permissions

**Issue**: Port 8501 already in use
- Solution: Run with a different port:
  ```bash
  streamlit run apps/debugging_assistant/app.py --server.port=8502
  ```

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please open an issue on the [GitHub repository](https://github.com/md-yahya1/debugging_assistant/issues).

---

**Made with ❤️ by [Mohammed Yahya](https://github.com/md-yahya1)**
