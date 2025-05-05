from pydantic import BaseModel
from typing import Optional

class OrderTrackingBase(BaseModel):
    status: str

class OrderTrackingCreate(OrderTrackingBase):
    order_id: int

class OrderTrackingUpdate(BaseModel):
    status: Optional[str] = None

class OrderTracking(OrderTrackingBase):
    order_id: int

    class ConfigDict:
        from_attributes = True