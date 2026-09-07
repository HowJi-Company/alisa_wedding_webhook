#!/bin/bash

echo "=== NEW STARTUP SCRIPT ==="
pwd
which uvicorn
which python
echo "$PATH"

exec uvicorn main:app \
  --host 0.0.0.0 \
  --port "${PORT:-8000}"
