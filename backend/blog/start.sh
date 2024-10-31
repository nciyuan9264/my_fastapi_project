#!/usr/bin/env bash
set -e

# 启动 Celery worker
exec poetry run celery -A blog.app.worker.celery_app worker -l info --hostname=worker1@%h -c 2 &
exec poetry run celery -A blog.app.worker.celery_app worker -l info --hostname=worker2@%h -c 2 &

# 启动 Uvicorn
exec poetry run uvicorn blog.app.main:app --host 0.0.0.0 --port 8000
