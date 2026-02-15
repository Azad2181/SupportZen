from app.db.models import Order

def get_order(db, order_id):
    return db.query(Order).filter(Order.order_id == order_id).first()