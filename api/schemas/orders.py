from datetime import datetime
from typing import List, Optional
from pydantic import Field, BaseModel
from .order_details import OrderDetail, OrderDetailCreate



class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None

class OrderCreate(OrderBase):
    order_details: List[OrderDetailCreate]

class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None

class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: List[OrderDetail] = Field(default_factory = list)

    class ConfigDict:
        from_attributes = True