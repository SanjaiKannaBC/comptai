from fastapi import FastAPI, Request
from .api import router as api_router
from .database import Base, engine
from .models import *
from .utils import get_request_id
from .config import settings

app = FastAPI(title="Comptai - Strategy Engine Skeleton")

# Create DB tables on startup (dev only)
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(api_router)

@app.middleware("http")
async def add_request_id_header(request: Request, call_next):
    rid = get_request_id(request)
    request.state.request_id = rid
    response = await call_next(request)
    response.headers["X-Request-Id"] = rid
    return response
