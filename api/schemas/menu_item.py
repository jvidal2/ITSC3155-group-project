from typing import Optional
from pydantic import BaseModel


class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    rating: Optional[int] = None


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    rating: Optional[int] = None


class MenuItem(MenuItemBase):
    itemID: int

    class Config:
        from_attributes = True
