from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    status = Column(String(50), nullable=False, server_default='inactive')
    order_id = Column(Integer, ForeignKey("order_details.id"))

    order_details = relationship("OrderDetail", back_populates="staff")
