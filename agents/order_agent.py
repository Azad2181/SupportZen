from app.services.llm_service import get_llm
from app.utils.prompts import SYSTEM_PROMPT

def handle_order_query(message: str):
    llm = get_llm()
    return llm.invoke([
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": message}
    ]).content