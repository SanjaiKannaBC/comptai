from celery import Celery
from app.config import settings

celery = Celery(
    "comptai_worker",
    broker=settings.CELERY_BROKER_URL,
)
celery.conf.task_routes = {
    "worker.worker_tasks.process_log": {"queue": "ingestion"}
}
