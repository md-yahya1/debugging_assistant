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

## Vercel Deployment

### Prerequisites
- [Vercel Account](https://vercel.com)
- [Vercel CLI](https://vercel.com/docs/cli) (optional, for CLI deployments)
- GitHub repository connected to Vercel

### Steps

1. **Connect Repository**
   - Go to [Vercel Dashboard](https://vercel.com/dashboard)
   - Click "Add New" → "Project"
   - Import your GitHub repository

2. **Configure Environment Variables**
   - Go to your project settings → Environment Variables
   - Add `HF_API_KEY` with your Hugging Face API token
   - Get your token from: https://huggingface.co/settings/tokens

3. **Deploy**
   - Vercel automatically deploys on push to the main branch
   - Monitor deployment in the Vercel dashboard
   - Your app will be available at a Vercel-provided URL (e.g. `your-project.vercel.app`)

4. **Set Custom Domain** (Optional)
   - In the Vercel dashboard, go to your project → Settings → Domains
   - Add your custom domain and follow the DNS configuration steps

### CLI Deployment (Alternative)
```bash
# Install Vercel CLI
npm install -g vercel

# Login and deploy
vercel login
vercel --prod
```

### Environment Variables
Set these in the Vercel dashboard or `.env` file:

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
- Check if `HF_API_KEY` is configured (in `.env` locally, or Vercel Environment Variables when deployed)
- Check if the model `Qwen/Qwen2.5-Coder-32B-Instruct` is still available on HF Inference API
- View logs in the Vercel dashboard under the **Deployments** tab → **Functions** logs

### YAML Parse Error on Startup
- Ensure `config/config.yaml` has valid YAML syntax
- Must use spaces for indentation (not tabs)
- Must not have duplicate top-level keys (`model:`, `debugging_app:`)

### Port Issues
- Vercel manages port assignment automatically via the serverless runtime
- No manual port configuration is needed in `vercel.json`

### Health Check Failures
- Ensure the app is running with `/health` endpoint accessible
- Check Vercel function logs for startup errors
