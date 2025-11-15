import uuid
from fastapi import Request

def get_request_id(request: Request):
    rid = request.headers.get("X-Request-Id")
    if not rid:
        rid = str(uuid.uuid4())
    return rid

def normalize_text(text: str) -> str:
    # naive normalizer, replace with robust implementation later
    return " ".join(text.strip().split())
