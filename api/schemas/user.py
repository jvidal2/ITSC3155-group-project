from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    phone_number: int


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: Optional[str]=None
    email: Optional[str]=None
    phone_number: Optional[int]=None


class User(UserBase):
    user_id: int

    class ConfigDict:
        from_attributes = True