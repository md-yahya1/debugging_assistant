# Deployment Guide

## Local Testing

### Running Locally
```bash
pip install -r requirements.txt
python main.py
```

The server will start at `http://localhost:8000`

### Testing Endpoints
```bash
# Home page
curl http://localhost:8000/

# Health check
curl http://localhost:8000/health

# Debug API (POST)
curl -X POST http://localhost:8000/api/debug \
  -H "Content-Type: application/json" \
  -d '{"code": "print(Hello World)"}'

# Code Generation API (POST)
curl -X POST http://localhost:8000/api/generate-code \
  -H "Content-Type: application/json" \
  -d '{"request": "Create a fibonacci function", "language": "python"}'
```

## Docker Deployment

### Build Docker Image
```bash
docker build -t debugging-assistant:latest .
```

### Run Docker Container
```bash
docker run -p 8000:8000 --env-file .env debugging-assistant:latest
```

## Railway Deployment

### Prerequisites
- [Railway Account](https://railway.app)
- GitHub repository connected to Railway

### Steps

1. **Connect Repository**
   - Go to [Railway Dashboard](https://railway.app/dashboard)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Connect your GitHub account and select this repository

2. **Configure Environment Variables**
   - Go to your project settings → Variables
   - Add `HF_API_KEY` with your Hugging Face API token
   - Get your token from: https://huggingface.co/settings/tokens

3. **Deploy**
   - Railway automatically deploys on push to main branch
   - Monitor deployment in the Railway dashboard
   - Your app will be available at a Railway-provided URL

4. **Set Custom Domain** (Optional)
   - In Railway dashboard, go to Settings → Domains
   - Add your custom domain

### Environment Variables
Set these in Railway dashboard or `.env` file:

```
HF_API_KEY=your_huggingface_api_token_here
```

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                Client Browser                        │
├─────────────────────────────────────────────────────┤
│                    Requests                          │
├─────────────────────────────────────────────────────┤
│              FastAPI Web Server                      │
│         (apps/debugging_assistant/app.py)            │
├─────────────────────────────────────────────────────┤
│                                                      │
│  ┌──────────────┐     ┌─────────────────────────┐  │
│  │  Static      │     │   API Endpoints         │  │
│  │  Assets      │     │                         │  │
│  │  (HTML/CSS/  │     │  - GET  /               │  │
│  │   JS)        │     │  - GET  /health         │  │
│  │              │     │  - POST /api/debug      │  │
│  │              │     │  - POST /api/generate-  │  │
│  │              │     │         code            │  │
│  └──────────────┘     └─────────────────────────┘  │
│                              │                      │
│                              ▼                      │
│                  ┌────────────────────┐             │
│                  │  HuggingFace API   │             │
│                  │  Qwen/Qwen2.5-    │             │
│                  │  Coder-32B-       │             │
│                  │  Instruct         │             │
│                  └────────────────────┘             │
│                                                     │
└─────────────────────────────────────────────────────┘
```

## Troubleshooting

### 500 Error on /api/debug
- Check if `HF_API_KEY` is configured (in `.env` locally, or Railway Variables when deployed)
- Check if the model `Qwen/Qwen2.5-Coder-32B-Instruct` is still available on HF Inference API
- View logs in Railway dashboard

### YAML Parse Error on Startup
- Ensure `config/config.yaml` has valid YAML syntax
- Must use spaces for indentation (not tabs)
- Must not have duplicate top-level keys (`model:`, `debugging_app:`)

### Port Issues
- Railway uses dynamic port assignment; the app listens on port 8000 by default
- The Dockerfile exposes port 8000

### Health Check Failures
- Ensure the app is running with `/health` endpoint accessible
- Check Railway logs for startup errors
