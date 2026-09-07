#!/bin/bash

echo "=== DEBUG ==="
pwd
which python
which uvicorn

echo "=== UVICORN SHEBANG ==="
head -n 1 "$(which uvicorn)"

echo "=== VENV PYTHON ==="
ls -la /app/.venv/bin/python*
readlink -f /app/.venv/bin/python || true

echo "=== MISE PYTHON ==="
ls -la /mise/installs/python/*/bin/python* || true

echo "=== PATH ==="
echo "$PATH"

exec uvicorn main:app \
  --host 0.0.0.0 \
  --port "${PORT:-8000}"
