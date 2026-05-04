<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:1a1a4e,100:0d0d2b&height=220&section=header&text=AI%20Debug%20Assistant&fontSize=52&fontColor=ffffff&fontAlignY=38&desc=%F0%9F%A4%96%20Paste%20your%20error.%20Get%20your%20fix.%20Ship%20faster.&descSize=17&descAlignY=60&animation=fadeIn" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Powered-FFD21F?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](#-docker-deployment)
[![Vercel](https://img.shields.io/badge/Vercel-Deploy-000000?style=for-the-badge&logo=vercel&logoColor=white)](#-vercel-deployment)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Issues](https://img.shields.io/github/issues/md-yahya1/debugging_assistant?style=for-the-badge&color=ef4444&labelColor=0d1117)](https://github.com/md-yahya1/debugging_assistant/issues)
[![Stars](https://img.shields.io/github/stars/md-yahya1/debugging_assistant?style=for-the-badge&color=f59e0b&labelColor=0d1117)](https://github.com/md-yahya1/debugging_assistant/stargazers)

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=18&duration=2800&pause=900&color=818CF8&center=true&vCenter=true&width=580&lines=Paste+error+%E2%86%92+Get+AI+explanation+%E2%9C%85;Generate+code+from+natural+language+%F0%9F%92%BB;Supports+any+language+or+framework+%F0%9F%9B%A0%EF%B8%8F;Powered+by+Qwen+2.5+Coder+%F0%9F%A4%96" />

</div>

---

## 🧠 What Is This?

**AI Debug Assistant** is a lightweight, LLM-powered debugging and code generation tool built with **FastAPI** and **Hugging Face**. Drop in your error log or broken code snippet — and get an instant, intelligent breakdown of what went wrong and how to fix it. Need new code? Describe what you want and get production-ready code generated instantly.

> Built for developers who are tired of Googling the same stack traces over and over.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🤖 **LLM-Powered Debugging** | Leverages Hugging Face's `Qwen/Qwen2.5-Coder-32B-Instruct` model to understand errors contextually |
| 💻 **Code Generation** | Describe what you need in plain English — get clean, working code in any language |
| 🌐 **Modern Web UI** | FastAPI backend with a sleek, responsive HTML/CSS/JS frontend |
| ⚙️ **YAML Config** | Swap models, tune temperature, set token limits — all from `config.yaml` |
| 🐳 **Docker-First** | One command to build, one command to run |
| ▲ **Vercel Deployed** | Ready for one-click deployment on Vercel |
| 🔒 **Secure by Design** | API keys via `.env`, never hardcoded, `.gitignore`d by default |
| ⚡ **Fast Inference** | Optimized prompt pipeline for snappy response times |
| 🩺 **Health Check** | Built-in `/health` endpoint for monitoring and uptime checks |

---

## 📸 Demo

<!-- Add a GIF or screenshot of the app in action here -->
```
📌 Screenshot / GIF coming soon
   → Run the app and grab a screen recording!
```

---

## 🛠️ Tech Stack

<div align="center">

**Core**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-Config-CB171E?style=for-the-badge&logo=yaml&logoColor=white)

**AI / ML**

![Hugging Face](https://img.shields.io/badge/HuggingFace-FFD21F?style=for-the-badge&logo=huggingface&logoColor=black)
![Qwen](https://img.shields.io/badge/Qwen_2.5_Coder-7C3AED?style=for-the-badge&logoColor=white)

**Frontend**

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

**DevOps**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

</div>

---

## 📁 Project Structure

```bash
debugging_assistant/
│
├── apps/
│   └── debugging_assistant/
│       ├── app.py              # 🚀 FastAPI application (routes & endpoints)
│       ├── prompts.py          # 💬 Prompt definitions
│       └── static/             # 🎨 Frontend assets
│           ├── index.html      #    Main HTML page
│           ├── styles.css      #    Stylesheet
│           └── script.js       #    Client-side logic
│
├── config/
│   ├── config.yaml             # ⚙️  Model + app settings (edit here)
│   └── model_config.py         # 🐍 Python config loader (Pydantic)
│
├── utils/
│   ├── llm_client.py           # 🤖 HuggingFace InferenceClient wrapper
│   ├── debugging_helper.py     # 🔍 Debug prompt builder
│   ├── code_generator_helper.py# 💻 Code generation prompt builder
│   ├── text_helpers.py         # 🔤 Text preprocessing utilities
│   └── prompts/                # 📝 Modular prompt templates (JSON)
│
├── .env.example                # 🔑 Environment variable template
├── requirements.txt            # 📦 Python dependencies
├── Dockerfile                  # 🐳 Container configuration
├── vercel.json                 # ▲ Vercel deployment config
├── main.py                     # 🏁 Main entry point (starts uvicorn)
└── README.md
```

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Serves the web UI |
| `GET` | `/health` | Health check — returns `{"status": "ok"}` |
| `POST` | `/api/debug` | Debug code/error logs |
| `POST` | `/api/generate-code` | Generate code from natural language |

### Request Examples

**Debug Code:**
```bash
curl -X POST http://localhost:8000/api/debug \
  -H "Content-Type: application/json" \
  -d '{"code": "print(Hello World)"}'
```

**Generate Code:**
```bash
curl -X POST http://localhost:8000/api/generate-code \
  -H "Content-Type: application/json" \
  -d '{"request": "Create a function to reverse a linked list", "language": "python"}'
```

---

## ⚡ Quick Start (Local)

**Get running in under 2 minutes:**

```bash
# 1. Clone the repo
git clone https://github.com/md-yahya1/debugging_assistant.git
cd debugging_assistant

# 2. Create & activate virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your API key
cp .env.example .env
# → Open .env and paste your Hugging Face API key

# 5. Launch 🚀
python main.py
```

Open **http://localhost:8000** in your browser. Done.

---

## 🐳 Docker Deployment

```bash
# Build the image
docker build -t debugging-assistant .

# Run the container
docker run -p 8000:8000 --env-file .env debugging-assistant
```

> App available at **http://localhost:8000**

---

## ▲ Vercel Deployment

This project ships with a `vercel.json` config for seamless deployment on [Vercel](https://vercel.com).

### Steps

1. **Push your repo to GitHub** (make sure `vercel.json` is at the root)

2. **Go to [vercel.com](https://vercel.com)** → Add New → Project → Import your GitHub repo

3. **Connect your GitHub repo** — Vercel will auto-detect `vercel.json`

4. **Set the environment variable** in the Vercel dashboard under **Settings → Environment Variables**:

   | Key | Value |
   |---|---|
   | `HF_API_KEY` | Your Hugging Face API token |

5. **Deploy** — Vercel builds and gives you a live URL (e.g. `your-project.vercel.app`)

> ⚠️ **Note:** Make sure your `HF_API_KEY` environment variable is set in Vercel's dashboard under **Environment Variables**. The app will fail to start without it.

### CLI Deployment (Alternative)
```bash
# Install Vercel CLI
npm install -g vercel

# Login and deploy
vercel login
vercel --prod
```

---

## 🔑 Environment Variables

Create a `.env` file locally from the template:

```bash
cp .env.example .env
```

```env
# .env
HF_API_KEY=your_huggingface_api_token_here
```

| Variable | Description | Required |
|---|---|---|
| `HF_API_KEY` | Hugging Face API token — get yours [here](https://huggingface.co/settings/tokens) | ✅ Yes |

> ⚠️ **Never commit your `.env` file.** It's already in `.gitignore`. On Vercel, set this in the dashboard under **Settings → Environment Variables**.

---

## ⚙️ Configuration

All model behavior is controlled from `config/config.yaml`:

```yaml
# config/config.yaml — customize to your needs
model:
  provider: huggingface
  name: "Qwen/Qwen2.5-Coder-32B-Instruct"   # swap any HF-supported model here
  temperature: 0.4
  top_p: 0.9
  max_output_tokens: 512

debugging_app:
  explanation_language: "en"
  max_code_chars: 4000
```

### Supported Models (Tested & Working)

| Model | Best For |
|---|---|
| `Qwen/Qwen2.5-Coder-32B-Instruct` | 🏆 Code debugging & generation (recommended) |
| `HuggingFaceH4/zephyr-7b-beta` | General-purpose chat |
| `meta-llama/Llama-3.1-8B-Instruct` | General-purpose reasoning |

> 💡 Not all Hugging Face models are available on the free serverless Inference API. If you get a `model_not_supported` error, switch to one of the models listed above.

---

## 🔧 Troubleshooting

<details>
<summary><b>❌ model_not_supported — "The requested model is not supported by any provider"</b></summary>

The model you specified in `config/config.yaml` is not available on HF's free serverless Inference API. Switch to a supported model:
```yaml
model:
  name: "Qwen/Qwen2.5-Coder-32B-Instruct"
```
See the [Supported Models](#supported-models-tested--working) table above.
</details>

<details>
<summary><b>❌ YAML parse error — "expected block end, but found block mapping start"</b></summary>

Your `config/config.yaml` has invalid YAML syntax. Common causes:
- Duplicate keys (e.g., two `model:` blocks)
- Incorrect indentation (must use spaces, not tabs)
- Missing newline between sections

Refer to the [Configuration](#️-configuration) section for the correct format.
</details>

<details>
<summary><b>❌ FileNotFoundError: Debugging prompt file not found</b></summary>

Make sure you're running the app from the **project root**, not a subdirectory:
```bash
cd debugging_assistant   # ← must be here
python main.py
```
</details>

<details>
<summary><b>❌ HF_API_KEY not found / Authentication error</b></summary>

- Double-check your `HF_API_KEY` in `.env` (local) or Vercel dashboard under **Settings → Environment Variables** (deployed)
- Ensure the key has **Inference** permissions enabled on [Hugging Face](https://huggingface.co/settings/tokens)
- Test your key:
```bash
curl https://huggingface.co/api/whoami -H "Authorization: Bearer YOUR_KEY"
```
</details>

<details>
<summary><b>❌ Port 8000 already in use</b></summary>

Another process is using port 8000. Either stop it or change the port in `main.py`:
```python
uvicorn.run(app, host="0.0.0.0", port=8001)  # use a different port
```
</details>

---

## 🗺️ Roadmap

- [x] Core LLM debugging pipeline
- [x] Code generation endpoint
- [x] YAML-based model configuration
- [x] FastAPI + static frontend
- [x] Docker support
- [x] Environment variable security
- [x] Vercel deployment config
- [x] Health check endpoint
- [ ] Multi-language support (Python, JS, Java, C++)
- [ ] Chat history & session memory
- [ ] Model selector dropdown in UI
- [ ] Export debug report as `.md` or `.pdf`
- [ ] GitHub Copilot-style inline fix suggestions
- [ ] Rate limiting & usage analytics

---

## 🤝 Contributing

Contributions are welcome and appreciated!

```bash
# 1. Fork the repository
# 2. Create your feature branch
git checkout -b feature/your-feature-name

# 3. Commit your changes
git commit -m "feat: add your feature description"

# 4. Push and open a PR
git push origin feature/your-feature-name
```

Good first contributions: bug fixes, new prompt templates, UI improvements, docs, or adding support for more LLM providers.

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

---

<div align="center">

**Built with 🧠 + ☕ by [Mohammed Yahya](https://github.com/md-yahya1)**

[![GitHub](https://img.shields.io/badge/GitHub-md--yahya1-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/md-yahya1)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mohammed-yahya-4b9879326)

<br/>

⭐ **If this saved you time, drop a star — it helps more developers find it!** ⭐

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d0d2b,50:1a1a4e,100:0f0c29&height=100&section=footer" width="100%"/>

</div>
