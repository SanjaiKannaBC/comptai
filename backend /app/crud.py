from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy import select

def create_behavior_log(db: Session, log: schemas.BehaviorLogCreate):
    obj = models.BehaviorLog(
        user_id=log.user_id,
        type=log.type,
        content_raw=log.content_raw,
        status="queued"
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def mark_log_processed(db: Session, log_id, content_norm=None, embedding_ref=None):
    q = db.get(models.BehaviorLog, log_id)
    if not q:
        return None
    if content_norm:
        q.content_norm = content_norm
    if embedding_ref:
        q.embedding_ref = embedding_ref
    q.status = "processed"
    db.add(q)
    db.commit()
    db.refresh(q)
    return q
