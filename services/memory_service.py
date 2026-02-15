import redis
from app.config import settings

redis_client = redis.from_url(settings.REDIS_URL)

def save_message(session_id: str, message: str):
    redis_client.rpush(session_id, message)

def get_history(session_id: str):
    history = redis_client.lrange(session_id, 0, -1)
    return [h.decode() for h in history]