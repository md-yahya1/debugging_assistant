<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:1a1a4e,100:0d0d2b&height=220&section=header&text=AI%20Debug%20Assistant&fontSize=52&fontColor=ffffff&fontAlignY=38&desc=%F0%9F%A4%96%20Paste%20your%20error.%20Get%20your%20fix.%20Ship%20faster.&descSize=17&descAlignY=60&animation=fadeIn" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Powered-FFD21F?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](#-docker-deployment)
[![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render&logoColor=black)](#-render-deployment)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Issues](https://img.shields.io/github/issues/md-yahya1/debugging_assistant?style=for-the-badge&color=ef4444&labelColor=0d1117)](https://github.com/md-yahya1/debugging_assistant/issues)
[![Stars](https://img.shields.io/github/stars/md-yahya1/debugging_assistant?style=for-the-badge&color=f59e0b&labelColor=0d1117)](https://github.com/md-yahya1/debugging_assistant/stargazers)

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=18&duration=2800&pause=900&color=818CF8&center=true&vCenter=true&width=580&lines=Paste+error+%E2%86%92+Get+AI+explanation+%E2%9C%85;Supports+any+language+or+framework+%F0%9F%9B%A0%EF%B8%8F;Deployed+on+Render+%F0%9F%9A%80;Powered+by+Hugging+Face+LLMs+%F0%9F%A4%96" />

</div>

---

## 🧠 What Is This?

**AI Debug Assistant** is a lightweight, LLM-powered debugging tool built with Streamlit and Hugging Face. Drop in your error log or broken code snippet — and get an instant, intelligent breakdown of what went wrong and how to fix it.

> Built for developers who are tired of Googling the same stack traces over and over.

---

## ✨ Key Features

- 🤖 **LLM-Powered Analysis** — Leverages Hugging Face inference models to understand errors contextually, not just pattern-match
- 💬 **Clean Web UI** — Streamlit-based interface; no frontend setup, zero friction
- ⚙️ **YAML Config** — Swap models, tune temperature, set token limits — all from `config.yaml`
- 🐳 **Docker-First** — One command to build, one command to run
- 🚀 **Render Deployed** — Live on the internet via Render's free tier
- 🔒 **Secure by Design** — API keys via `.env`, never hardcoded, `.gitignore`d by default
- ⚡ **Fast Inference** — Optimized prompt pipeline for snappy response times

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
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-Config-CB171E?style=for-the-badge&logo=yaml&logoColor=white)

**AI / ML**

![Hugging Face](https://img.shields.io/badge/HuggingFace-FFD21F?style=for-the-badge&logo=huggingface&logoColor=black)

**DevOps**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

</div>

---

## 📁 Project Structure

```bash
debugging_assistant/
│
├── apps/
│   └── debugging_assistant/
│       ├── app.py              # 🚀 Main Streamlit entry point
│       └── prompts.py          # 💬 Prompt definitions
│
├── config/
│   ├── config.yaml             # ⚙️  Model + app settings (edit here)
│   └── model_config.py         # 🐍 Python config loader
│
├── utils/
│   ├── debugging_helper.py     # 🔍 Core debugging logic
│   ├── llm_client.py           # 🤖 HuggingFace API client
│   ├── text_helpers.py         # 🔤 Text preprocessing utilities
│   └── prompts/                # 📝 Modular prompt templates
│
├── .env.example                # 🔑 Environment variable template
├── requirements.txt            # 📦 Python dependencies
├── Dockerfile                  # 🐳 Container configuration
├── render.yaml                 # 🚀 Render deployment blueprint
└── README.md
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
streamlit run apps/debugging_assistant/app.py
```

Open **http://localhost:8501** in your browser. Done.

---

## 🐳 Docker Deployment (Local)

```bash
# Build the image
docker build -t debugging-assistant .

# Run the container
docker run -p 8501:8501 --env-file .env debugging-assistant
```

> App available at **http://localhost:8501**

---

## 🚀 Render Deployment

This project ships with a `render.yaml` blueprint for one-click deployment on [Render](https://render.com).

### Steps

1. **Push your repo to GitHub** (make sure `render.yaml` and `Dockerfile` are at the root)

2. **Go to [render.com](https://render.com)** → New → Blueprint

3. **Connect your GitHub repo** — Render will auto-detect `render.yaml`

4. **Set the environment variable** in the Render dashboard:

   | Key | Value |
   |---|---|
   | `HF_API_KEY` | Your Hugging Face API token |

5. **Deploy** — Render builds the Docker image and gives you a live URL like:
   ```
   https://ai-debug-assistant.onrender.com
   ```

> ⚠️ **Free tier note:** Render's free instances spin down after 15 minutes of inactivity. The first request after sleep may take ~30 seconds to wake up.

### Manual Deploy (without Blueprint)

If you prefer to configure manually on Render:

- **Environment:** Docker
- **Dockerfile path:** `./Dockerfile`
- **Instance type:** Free (or Starter for always-on)
- **Environment variable:** `HF_API_KEY` = your token

---

## 🔑 Environment Variables

Create a `.env` file locally from the template:

```bash
cp .env.example .env
```

```env
# .env.example
HF_API_KEY=your_huggingface_api_token_here
```

| Variable | Description | Required |
|---|---|---|
| `HF_API_KEY` | Hugging Face API token — get yours [here](https://huggingface.co/settings/tokens) | ✅ Yes |

> ⚠️ **Never commit your `.env` file.** It's already in `.gitignore`. On Render, set this in the dashboard under **Environment**.

---

## ⚙️ Configuration

All model behavior is controlled from `config/config.yaml`:

```yaml
# config/config.yaml — customize to your needs
model:
  provider: huggingface
  name: "Qwen/Qwen2.5-1.5B-Instruct"   # swap any HF model here
  temperature: 0.4
  max_new_tokens: 512
  top_p: 0.9

debugging_app:
  max_code_chars: 4000
  explanation_language: "en"
```

---

## 🔧 Troubleshooting

<details>
<summary><b>❌ FileNotFoundError: Debugging prompt file not found</b></summary>

Make sure you're running the app from the **project root**, not a subdirectory:
```bash
cd debugging_assistant   # ← must be here
streamlit run apps/debugging_assistant/app.py
```
</details>

<details>
<summary><b>❌ HFValidationError: Could not connect to Hugging Face</b></summary>

- Double-check your `HF_API_KEY` in `.env` (local) or Render dashboard (deployed)
- Ensure the key has **Inference** permissions enabled on Hugging Face
- Test your key: `curl https://huggingface.co/api/whoami -H "Authorization: Bearer YOUR_KEY"`
</details>

<details>
<summary><b>❌ Render deploy fails — port binding error</b></summary>

Render injects a `$PORT` environment variable at runtime. The `Dockerfile` already handles this:
```dockerfile
CMD streamlit run apps/debugging_assistant/app.py --server.port=$PORT ...
```
Make sure you're using the updated `Dockerfile` from this repo.
</details>

<details>
<summary><b>❌ Port 8501 already in use (local)</b></summary>

```bash
streamlit run apps/debugging_assistant/app.py --server.port=8502
```
</details>

---

## 🗺️ Roadmap

- [x] Core LLM debugging pipeline
- [x] YAML-based model configuration
- [x] Docker support
- [x] Environment variable security
- [x] Render deployment
- [ ] Multi-language support (Python, JS, Java, C++)
- [ ] Chat history & session memory
- [ ] Model selector dropdown in UI
- [ ] Export debug report as `.md` or `.pdf`
- [ ] GitHub Copilot-style inline fix suggestions

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
