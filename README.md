# Comptai — AI Personal Strategy Engine (skeleton)

This repo contains the initial FastAPI + Celery skeleton for the Comptai project.

## Dev quickstart

1. Install Docker & Docker Compose.
2. `git clone <repo>`
3. `docker-compose up --build`
4. Backend runs at `http://localhost:8000`. Use POST `/api/v1/logs` to create a log.

Example payload:
```json
{
  "user_id": "00000000-0000-0000-0000-000000000001",
  "type": "reflection",
  "content_raw": "Today I planned to study but watched videos instead."
}
