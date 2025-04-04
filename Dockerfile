# ---- Base Python image ----
FROM python:3.12-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# ---- Install system dependencies ----
RUN apt-get update \
    && apt-get install -y netcat-openbsd gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ---- Install Python dependencies ----
COPY pyproject.toml poetry.lock ./
RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --only main

# ---- Copy project files ----
COPY . .

# ---- Collect static (safe at build) ----
RUN python manage.py collectstatic --noinput

# ---- Create app user ----
RUN adduser --disabled-password --no-create-home appuser

# ---- Entrypoint (runs migrations & server) ----
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER appuser

ENTRYPOINT ["/entrypoint.sh"]

