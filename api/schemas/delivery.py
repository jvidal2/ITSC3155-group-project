from pydantic import BaseModel
from typing import Optional


class DeliveryBase(BaseModel):
    name: str
    address: str


class DeliveryCreate(DeliveryBase):
    pass


class DeliveryUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None


class Delivery(DeliveryBase):
    id: int

    class Config:
        from_attributes = True
