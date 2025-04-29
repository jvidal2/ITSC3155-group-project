from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ReviewBase(BaseModel):
    customer_id: int
    menu_item_id: int
    rating: int
    review_text: Optional[str] = None
    image_included: Optional[bool] = None


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    rating: Optional[int] = None
    review_text: Optional[str] = None
    image_included: Optional[bool] = None


class Review(ReviewBase):
    id: int
    created_at: datetime

    class ConfigDict:
        orm_mode = True