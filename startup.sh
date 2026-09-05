#!/bin/bash
# startup.sh — 啟動 FastAPI 婚禮小幫手後端

WEB_CONCURRENCY="${WEB_CONCURRENCY:-2}"
GUNICORN_TIMEOUT="${GUNICORN_TIMEOUT:-120}"
PORT="${PORT:-8000}"

/app/.venv/bin/python -m gunicorn \
  -w "${WEB_CONCURRENCY}" \
  -k uvicorn.workers.UvicornWorker \
  main:app \
  --bind "0.0.0.0:${PORT}" \
  --timeout "${GUNICORN_TIMEOUT}"
