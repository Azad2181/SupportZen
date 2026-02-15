from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest
from app.agents.router import route_query
from app.services.memory_service import save_message

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/")
async def chat(request: ChatRequest):
    response = route_query(request.message)
    save_message(request.session_id, request.message)
    save_message(request.session_id, response)
    return {"response": response}