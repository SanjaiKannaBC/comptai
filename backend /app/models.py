from sqlalchemy import Column, String, Text, Integer, DateTime, Float, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB, ARRAY
from sqlalchemy.sql import func
import uuid
from .database import Base
import enum

class LogType(str, enum.Enum):
    task = "task"
    reflection = "reflection"
    decision = "decision"
    micro_action = "micro_action"

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(256), unique=True, nullable=False)
    hashed_password = Column(String(512), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class BehaviorLog(Base):
    __tablename__ = "behavior_logs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    type = Column(Enum(LogType), nullable=False)
    content_raw = Column(Text, nullable=False)
    content_norm = Column(Text, nullable=True)
    tags = Column(JSONB, nullable=True)
    mood_score = Column(Float, nullable=True)
    energy_score = Column(Integer, nullable=True)
    embedding_ref = Column(String, nullable=True)
    status = Column(String(32), default="queued")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
