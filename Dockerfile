FROM python:3.11-slim

WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "apps/debugging_assistant/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
