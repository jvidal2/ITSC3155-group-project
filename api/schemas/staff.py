from typing import Optional
from pydantic import BaseModel

class StaffBase(BaseModel):
    name: Optional[str] = None
    status: str
    order_id: int

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