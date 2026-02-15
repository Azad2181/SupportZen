from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.health import router as health_router
from app.core.logging_config import logger

app = FastAPI(title="SupportZen")

app.include_router(chat_router)
app.include_router(health_router)

@app.on_event("startup")
def startup():
    logger.info("SupportZen application started successfully.")