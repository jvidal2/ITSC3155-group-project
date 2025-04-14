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
    user_id: int


class User(UserBase):
    id: int

    class ConfigDict:
        from_attributes = True