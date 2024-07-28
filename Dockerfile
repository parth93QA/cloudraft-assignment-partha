# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.11.4
FROM python:${PYTHON_VERSION}-slim as base
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt


FROM base as cloudraft_kv_test
WORKDIR /app
COPY . .
RUN pytest test_main.py


FROM base as final_kv_image
WORKDIR /app
COPY . .
EXPOSE 8080
CMD  uvicorn main:app --host 0.0.0.0 --port 8080 --workers 4
