from typing import Optional
from pydantic import BaseModel

class StaffBase(BaseModel):
    name: str
    status: str
    order_id: Optional[int] = None

class StaffCreate(StaffBase):
    pass

class StaffUpdate(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None
    order_id: Optional[int] = None

class Staff(StaffBase):
    id: int
    
    class ConfigDict:
        from_attributes = True