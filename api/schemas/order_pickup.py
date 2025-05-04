from pydantic import BaseModel
from typing import Optional


class OrderPickupBase(BaseModel):
    name: str
    address: str


class OrderPickupCreate(OrderPickupBase):
    pass


class OrderPickupUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None


class OrderPickup(OrderPickupBase):
    id: int

    class ConfigDict:
        from_attributes = True
