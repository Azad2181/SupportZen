from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#you can create more class here as needed
class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True)
    order_status = Column(String)
    delivery_status = Column(String)