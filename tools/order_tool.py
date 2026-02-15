def fetch_order_status(order_id, db):
    order = db.query(Order).filter(Order.order_id == order_id).first()
    if not order:
        return "Order not found."
    return f"Order Status: {order.order_status}, Delivery: {order.delivery_status}"