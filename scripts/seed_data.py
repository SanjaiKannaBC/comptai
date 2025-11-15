import requests
import uuid
from datetime import datetime

BASE = "http://localhost:8000/api/v1"

def seed_user_and_logs():
    # Create a fake user directly via DB or use an admin endpoint; for dev, create via DB script
    print("Seed scripts require you to create a user in DB manually or via psql.")
    # For simplicity, we assume a user_id environment variable for dev:
    user_id = "00000000-0000-0000-0000-000000000001"
    payload = {
        "user_id": user_id,
        "type": "reflection",
        "content_raw": "Today I planned to study data engineering but spent time on YouTube instead."
    }
    r = requests.post(f"{BASE}/logs", json=payload)
    print("Seed response:", r.status_code, r.text)

if __name__ == "__main__":
    seed_user_and_logs()
