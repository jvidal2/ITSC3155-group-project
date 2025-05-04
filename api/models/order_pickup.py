from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class OrderPickup(Base):
    __tablename__ = "order_pickup"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"))
    description = Column(String, ForeignKey("orders.description"))
    amount = Column(DECIMAL, ForeignKey("payment.amount"))
    payment_method = Column(String, ForeignKey("payment.method"))