from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    amount: float
    method: str
    status: str
    promo_code: Optional[str] = None
    promo_applied: bool = False
    order_id: int


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    amount: Optional[float] = None
    method: Optional[str] = None
    status: Optional[str] = None
    promo_code: Optional[str] = None
    promo_applied: Optional[bool] = None


class Payment(PaymentBase):
    paymentID: int
    
    class ConfigDict:
        from_attributes = True