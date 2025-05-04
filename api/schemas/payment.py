from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    amount: float
    method: str
    status: str
    promo_code: Optional[str] = None
    promotion_id: Optional[int] = None


class PaymentCreate(PaymentBase):
    order_id: int


class PaymentUpdate(BaseModel):
    amount: Optional[float] = None
    method: Optional[str] = None
    status: Optional[str] = None
    promo_code: Optional[str] = None
    promotion_id: Optional[int] = None


class Payment(PaymentBase):
    paymentID: int
    order_id: int
    
    class ConfigDict:
        from_attributes = True