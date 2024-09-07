# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.11.4
FROM python:${PYTHON_VERSION}-slim as base
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt
WORKDIR /app
COPY . .
CMD uvicorn main:app --host 0.0.0.0 --port 8080






