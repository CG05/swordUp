import redis
import os
from app.models.weapon import Weapon
import json

_user_store = {
    "test": {
        "weapon_key": "sword1",
        "level": 0
    }
}

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True
)

def load_user(user_id: str) -> dict:
    if user_id not in _user_store:
        _user_store[user_id] = {
            "weapon_key": "sword1",
            "level": 0
        }
    return _user_store[user_id]
    #data = redis.get(user_id)
    #return json.loads(data)

def save_user(user_id: str, state: dict):
    _user_store[user_id] = state
    #redis.set(user_id, json.dumps(state))