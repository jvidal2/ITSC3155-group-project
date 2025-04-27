from datetime import date
from typing import Optional
from pydantic import BaseModel


class PromotionBase(BaseModel):
    name: str
    discount_percent: float
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    active: bool = True
    menu_item_id: Optional[int] = None


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    name: Optional[str] = None
    discount_percent: Optional[float] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    active: Optional[bool] = None
    menu_item_id: Optional[int] = None


class Promotion(PromotionBase):
    id: int

    class ConfigDict:
        from_attributes = True
