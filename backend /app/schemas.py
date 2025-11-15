from pydantic import BaseModel, Field
from typing import Optional, List
import uuid
from datetime import datetime
from .models import LogType

class BehaviorLogCreate(BaseModel):
    user_id: uuid.UUID
    type: LogType
    content_raw: str
    created_at: Optional[datetime] = None

class BehaviorLogOut(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    type: LogType
    content_raw: str
    content_norm: Optional[str]
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
