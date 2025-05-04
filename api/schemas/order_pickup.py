from pydantic import BaseModel
from typing import Optional


class OrderPickupBase(BaseModel):
    name: str
    order_id: int
    description: str
    amount: int
    payment_method: str


class OrderPickupCreate(OrderPickupBase):
    pass


class OrderPickupUpdate(BaseModel):
    name: Optional[str] = None
    payment_method: Optional[str] = None


class OrderPickup(OrderPickupBase):
    id: int

    class Config:
        from_attributes = True
