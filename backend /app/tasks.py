from .database import SessionLocal
from . import crud, utils
import time
import uuid

def ingestion_job(log_id: str):
    # This is the worker-side job that normalizes and writes dummy embedding
    db = SessionLocal()
    try:
        log = db.get(crud.__dict__['models'].BehaviorLog, log_id)
        if not log:
            return {"status": "not_found"}
        content_norm = utils.normalize_text(log.content_raw)
        # simulate embedding creation (replace with real embedding call)
        embedding_ref = "emb-" + str(uuid.uuid4())
        # pretend we called LLM and got mood
        db_log = crud.mark_log_processed(db, log_id, content_norm=content_norm, embedding_ref=embedding_ref)
        return {"status": "ok", "log_id": str(log_id)}
    finally:
        db.close()
