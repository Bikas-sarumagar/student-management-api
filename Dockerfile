FROM python:3.12-slim

# Workdir
WORKDIR /app

# Keep Python output unbuffered, no .pyc
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# System deps for psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Collect static files at build-time (optional; harmless if none)
RUN python manage.py collectstatic --noinput || true

# Gunicorn will be launched by docker-compose/Render command
