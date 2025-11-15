from .celery_app import celery
from app.tasks import ingestion_job
from app.database import SessionLocal
import logging

logger = logging.getLogger(__name__)

@celery.task(name="worker.worker_tasks.process_log", bind=True, acks_late=True)
def process_log(self, log_id: str, request_id: str = None):
    logger.info("Starting ingestion job for %s request=%s", log_id, request_id)
    try:
        result = ingestion_job(log_id)
        logger.info("Ingestion result: %s", result)
        return result
    except Exception as exc:
        logger.exception("Error processing log %s", log_id)
        raise self.retry(exc=exc, countdown=5, max_retries=3)
