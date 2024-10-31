#!/usr/bin/env bash
set -e

# 启动 Celery worker
exec poetry run celery -A blog.app.worker.celery_app worker -l info -c 1 &

# 启动 Uvicorn
exec poetry run uvicorn blog.app.main:app --host 0.0.0.0 --port 8000
