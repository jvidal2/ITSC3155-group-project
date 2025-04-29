from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("users.user_id"))
    menu_item_id = Column(Integer, ForeignKey("menu_item.itemID"))
    rating = Column(Integer, nullable=True)
    review_text = Column(String(100), nullable=True)
    image_included = Column(Boolean, nullable=True)
    created_at = Column(DATETIME, default=datetime.utcnow)

    user = relationship("User", back_populates="reviews")
    menu_item = relationship("MenuItem", back_populates="reviews")
