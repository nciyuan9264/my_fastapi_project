# backend/celery_app.py
from celery import Celery
from . import celery_config
celery_app = Celery('backend_celery')
celery_app.config_from_object(celery_config)
