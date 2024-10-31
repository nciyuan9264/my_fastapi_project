# backend/tasks.py
import time
import random
from blog.app.core.celery_app import celery_app

@celery_app.task
def add(n):

    time.sleep(random.uniform(1, 5))  # 模拟随机延迟
    result = 0
    for i in range(n):
        result += (i ** 2) * random.uniform(0.1, 1.0)  # 复杂计算
    return result