from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .menu_item import MenuItem


class OrderDetailBase(BaseModel):
    amount: int


class OrderDetailCreate(OrderDetailBase):
    menu_item_id: int

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    menu_item_id: Optional[int] = None
    amount: Optional[int] = None
    third_party_delivery_service_id: Optional[int] = None

class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    menu_item: MenuItem = None

    class ConfigDict:
        from_attributes = True