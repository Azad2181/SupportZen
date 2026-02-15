import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("YOUR_OPENAI_API_KEY")
    DATABASE_URL = os.getenv("YOU_DATABASE_URL")
    REDIS_URL = os.getenv("YOUR_REDIS_URL")
    ENV = os.getenv("ENV", "dev")

settings = Settings()