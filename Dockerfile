# Multi-stage Dockerfile for super-octo-bassoon
# Stage 1: builder - Install dependencies and build wheel
FROM python:3.12-bookworm AS builder

# Install build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl git && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install 'poetry>=2.0.0'

# Install Poetry
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

# Copy only dependency files first for better layer caching
COPY pyproject.toml README.md /app/

# Install dependencies into in-project virtualenv (no root install needed)
RUN poetry install --no-interaction --no-root --only main && \
    rm -rf ${POETRY_CACHE_DIR}

# Copy source code
COPY src/ /app/src/

# Build wheel (optional but good for reproducibility)
RUN poetry build -f wheel && \
    pip wheel --no-deps dist/*.whl -w /tmp/wheels

# Stage 2: test - install dev dependencies and run quality checks & tests
FROM builder AS test

# Copy tests (and any future test resources) into image
COPY tests /app/tests

# Install dev dependencies (remove --only main constraint); include project itself for mypy/pytest
RUN poetry install --no-interaction

# Run linting, formatting checks, type checking, and tests with coverage.
# Each kept in a single RUN so build fails fast if any check fails.
RUN poetry run flake8 src tests \
    && poetry run black --check src tests \
    && poetry run isort --check-only src tests \
    && poetry run mypy src \
    && poetry run pytest --cov=src --cov-report=term-missing

# Stage 3: runtime - minimal image with only runtime dependencies and app wheel
FROM python:3.12-slim AS runtime
LABEL org.opencontainers.image.source="https://github.com/npena/super-octo-bassoon" \
      org.opencontainers.image.title="super-octo-bassoon" \
      org.opencontainers.image.description="A hello world Python project"

# Create non-root user
RUN useradd -m appuser
WORKDIR /app

COPY --from=builder /tmp/wheels /tmp/wheels
RUN pip install --no-cache-dir /tmp/wheels/*.whl && rm -rf /tmp/wheels

# Copy source (optional if wheel already contains it; kept for dev transparency)
COPY --from=builder /app/src /app/src

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 PATH="/usr/local/bin:$PATH"

USER appuser

ENTRYPOINT ["python", "-m", "super_octo_bassoon.cli"]
CMD []
