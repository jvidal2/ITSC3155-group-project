from sqlalchemy import Column, Integer, String, DECIMAL, Boolean
from sqlalchemy.orm import relationship

from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menu_item"

    itemID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(300))
    price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')
    rating = Column(Integer)
    available = Column(Boolean, nullable=False, default=True)

    reviews = relationship("Review", back_populates="menu_item")
    promotions = relationship("Promotion", back_populates="menu_item")