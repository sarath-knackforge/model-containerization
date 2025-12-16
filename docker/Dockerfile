FROM python:3.11-slim

WORKDIR /app

COPY docker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY LOCAL MODEL (baked into image)
COPY model /app/model

COPY docker/app.py /app/app.py

ENV MODEL_DIR=/app/model

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
