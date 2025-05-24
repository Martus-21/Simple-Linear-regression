# Stage 1: Builder for dependencies
FROM python:3.9-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Stage 2: Runtime
FROM python:3.9-slim

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    FLASK_APP=app/main.py \
    FLASK_ENV=production \
    PATH="/root/.local/bin:${PATH}"

# Install runtime dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Copy installed packages
COPY --from=builder /root/.local /root/.local

# Copy application
WORKDIR /app
ENV PYTHONPATH=/app
COPY . .

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:5000/ || exit 1

# Install test dependencies
RUN pip install --no-cache-dir pytest pytest-cov

# Expose port
EXPOSE 5000

# Single CMD instruction
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]