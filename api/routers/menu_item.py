from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import menu_item as controller
from ..schemas import menu_item as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Menu Items'],
    prefix="/menu_items"
)


@router.post("/", response_model=schema.MenuItem)
def create(request: schema.MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.MenuItem])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.MenuItem)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db=db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.MenuItem)
def update(item_id: int, request: schema.MenuItemUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, item_id=item_id, request=request)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)


#search and filter
@router.get("/search", response_model=list[schema.MenuItem])
def search_menu_items(q: str = "", exclude: str = "", db: Session = Depends(get_db)):
    return controller.search_menu_items(db=db, q=q, exclude=exclude)
