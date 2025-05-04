from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    paymentID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    amount = Column(DECIMAL(6, 2), nullable=False, default='0.00')
    method = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)
    promo_code = Column(String(50), nullable=True)

    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    order = relationship("Order", back_populates="payment")

    promotion_id = Column(Integer, ForeignKey("promotions.id"), nullable=True)
    promotion = relationship("Promotion", back_populates="payments")