# backend/celeryconfig.py
from kombu import Queue

broker_url = 'redis://redis:6379/0'
result_backend = 'redis://redis:6379/1'
include = ['blog.app.worker']
result_expires = 6000
broker_connection_retry_on_startup = True
enable_utc = False
timezone = 'Asia/Shanghai'

task_queues = (
    Queue('queue_1'),
    Queue('default_queue'),
)

task_routes = {
    # 'backend.tasks.task1.*': {'queue': 'queue_1'},
    '*': {'queue': 'default_queue'},
}
task_default_queue = 'default_queue'
