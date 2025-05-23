from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    discount_percent = Column(DECIMAL(5, 2), nullable=False)  # Example: 10.00 for 10% discount
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    active = Column(Boolean, default=True)
    menu_item_id = Column(Integer, ForeignKey("menu_item.itemID"), nullable=True)
    menu_item = relationship("MenuItem", back_populates="promotions")
    payments = relationship("Payment", back_populates="promotion")