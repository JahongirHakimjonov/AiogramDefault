# syntax=docker/dockerfile:1.2
ARG PYTHON_VERSION=3.11
ARG UV_VERSION=0.7.2

# Stage 1: uv binarini olish
FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv

# Stage 2: Builder
FROM python:${PYTHON_VERSION} AS builder
COPY --from=uv /uv /uvx /bin/

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    PYTHONBUFFERED=1

WORKDIR /app

# virtual environment yaratish va dependencies o‘rnatish
RUN uv venv /app/.venv
COPY ./pyproject.toml ./uv.lock ./
RUN uv sync --no-dev --frozen --no-install-project --group docker

# Stage 3: Runtime (app)
FROM python:${PYTHON_VERSION}-slim AS app

WORKDIR /app

# uv binarini ham runtime stage’ga ko‘chirish
COPY --from=uv /uv /uvx /bin/

# runtime dependencies
RUN pip install --no-cache-dir psycopg2-binary

# entrypoint va start skriptlarini ko‘chirish
COPY ./deployments/compose/backend/entrypoint /entrypoint
COPY ./deployments/compose/backend/start /start

# Skriptlarga ruxsat berish
RUN sed -i 's/\r$//g' /entrypoint /start && \
    chmod +x /entrypoint /start

ENV PYTHONBUFFERED=1
ENV PYTHONPATH=$PYTHONPATH:/app/src PATH=/app/.venv/bin:$PATH

# Builder’dan venv ni ko‘chirish
COPY --from=builder /app/.venv .venv

# pyproject va lock fayllarini qo‘shish
COPY ./pyproject.toml ./uv.lock ./

# qolgan loyihani ko‘chirish
COPY src .

# guruh ruxsatlarini sozlash
RUN chgrp -R 0 /app && chmod -R g=u /app

ENTRYPOINT ["/entrypoint"]
