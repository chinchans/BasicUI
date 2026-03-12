# syntax=docker/dockerfile:1
FROM python:3.12-slim

# 1) Security & reproducibility basics
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 2) System deps (only what we need)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# 3) Create app user & workdir
WORKDIR /app
RUN useradd -m appuser

# 4) Copy Python deps first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5) Copy app code
COPY app.py .

# 6) Switch to non-root
USER appuser

# 7) Expose and run
EXPOSE 8000
CMD ["python", "app.py"]
