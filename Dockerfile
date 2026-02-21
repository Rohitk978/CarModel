FROM python:3.10-slim

# Prevent python buffering logs (important for docker logs)
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000