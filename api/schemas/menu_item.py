from typing import Optional
from pydantic import BaseModel


class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    rating: Optional[int] = None
    available: Optional[bool] = True


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    rating: Optional[int] = None
    available: Optional[bool] = None

class MenuItem(MenuItemBase):
    itemID: int

    class ConfigDict:
        from_attributes = True