from pydantic import BaseModel
from typing import Optional


class ThirdPartyDeliveryServiceBase(BaseModel):
    name: str
    amount: float
    address: str
    status: str


class ThirdPartyDeliveryServiceCreate(ThirdPartyDeliveryServiceBase):
    pass


class ThirdPartyDeliveryServiceUpdate(BaseModel):
    name: Optional[str] = None
    amount: Optional[float] = None
    status: Optional[str] = None


class ThirdPartyDeliveryService(ThirdPartyDeliveryServiceBase):
    id: int

    class Config:
        from_attributes = True