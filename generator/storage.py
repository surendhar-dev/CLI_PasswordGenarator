import json
import os
from datetime import datetime

DB_FILE = "data/history.json"

def load_history() -> dict:
    if not os.path.exists(DB_FILE):
        return {"next_id": 1, "history": []}
    try:
        with open(DB_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {"next_id": 1, "history": []}

def save_password_record(password: str, strength_rating: str):
    data = load_history()
    record = {
        "id": data["next_id"],
        "password": password,
        "strength": strength_rating,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data["history"].append(record)
    data["next_id"] += 1

    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=2)

def clear_history():
    data = {"next_id": 1, "history": []}
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=2)