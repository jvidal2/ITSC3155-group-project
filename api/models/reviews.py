from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Reviews(Base):
    __tablename__ = "reviews"

    customer_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    rating = Column(Integer, unique=True, nullable=True)
    review_text = Column(String(100), nullable=True)
    image_included = Column(Boolean, unique=True, nullable=True)

    user = relationship("User", back_populates="reviews")
    menu_item = relationship("MenuItem", back_populates="reviews")
