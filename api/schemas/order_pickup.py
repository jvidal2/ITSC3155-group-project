from pydantic import BaseModel
from typing import Optional


class OrderPickupBase(BaseModel):
    name: str
    order_id: int
    payment_id: int


class OrderPickupCreate(OrderPickupBase):
    pass


class OrderPickupUpdate(BaseModel):
    name: Optional[str] = None

class OrderPickup(OrderPickupBase):
    id: int

    class Config:
        from_attributes = True
