from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class ThirdPartyDeliveryService(Base):
    __tablename__ = "third_party_delivery_service"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    amount = Column(DECIMAL(6, 2), nullable=False, default='0.00')
    address = Column(String(100), nullable=False)
    status = Column(String(50), nullable=False)

    order_details = relationship("OrderDetail", back_populates="third_party_delivery_service")