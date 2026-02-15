from app.agents.product_agent import handle_product_query
from app.agents.order_agent import handle_order_query
from app.agents.policy_agent import handle_policy_query
from app.agents.concierge_agent import handle_general_query


# you can create more agents for your need.
def route_query(message: str):
    lower = message.lower()

    if "order" in lower:
        return handle_order_query(message)
    elif "return" in lower or "exchange" in lower:
        return handle_policy_query(message)
    elif "size" in lower or "fabric" in lower:
        return handle_product_query(message)
    else:
        return handle_general_query(message)