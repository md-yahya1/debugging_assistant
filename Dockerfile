FROM python:3.11-slim

WORKDIR /app

# Copy requirements first (better layer caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Render assigns a dynamic port via the PORT env variable
EXPOSE 8501

# Use shell form so $PORT is expanded at runtime
CMD streamlit run apps/debugging_assistant/app.py \
    --server.port=$PORT \
    --server.address=0.0.0.0 \
    --server.headless=true \
    --server.enableCORS=false \
    --server.enableXsrfProtection=false