from fastapi import APIRouter, Depends, HTTPException, Request, BackgroundTasks
from .schemas import BehaviorLogCreate, BehaviorLogOut
from .database import get_db
from sqlalchemy.orm import Session
from . import crud, utils
from worker.celery_app import celery

router = APIRouter(prefix="/api/v1")

@router.post("/logs", response_model=BehaviorLogOut)
def create_log(payload: BehaviorLogCreate, request: Request, db: Session = Depends(get_db)):
    request_id = utils.get_request_id(request)
    # Create the DB row
    obj = crud.create_behavior_log(db, payload)
    # enqueue celery job
    celery.send_task("worker.worker_tasks.process_log", args=[str(obj.id), request_id])
    return obj
