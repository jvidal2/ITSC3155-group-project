from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class OrderTracking(Base):
    __tablename__ = "order_tracking"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), unique=True)
    status = Column(String(50), nullable=False, default="received")
    last_updated = Column(DateTime, nullable=False, default=datetime.now())
    
    order = relationship("Order", back_populates="tracking")