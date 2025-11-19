FROM python:3.12-slim as builder

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy application code
COPY main.py ./main.py

# Copy project files
COPY pyproject.toml ./pyproject.toml
COPY uv.lock ./uv.lock

# Install project
RUN uv sync --locked

# Expose the port
EXPOSE 8000

# Run the application
CMD ["uv", "run","fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8000"]
