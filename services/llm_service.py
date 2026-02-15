from langchain_openai import ChatOpenAI
from app.config import settings

# LLM Service (you can replace this with any other LLM provider or model)
def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2,
        openai_api_key=settings.OPENAI_API_KEY
    )