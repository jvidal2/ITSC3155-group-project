from typing import Optional
from pydantic import BaseModel

class AdministrationBase(BaseModel):
    status: str
    name: str


class AdministrationCreate(AdministrationBase):
    pass


class AdministrationUpdate(BaseModel):
    status: Optional[str] = None
    name: Optional[str] = None


class Administration(AdministrationBase):
    admin_ID: int

    class ConfigDict:
        from_attributes = True