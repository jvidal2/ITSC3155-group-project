from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import third_party_delivery_service as controller
from ..schemas import third_party_delivery_service as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['ThirdPartyDeliveryServices'],
    prefix="/third-party-delivery-services"
)


@router.post("/", response_model=schema.ThirdPartyDeliveryService)
def create(
    request: schema.ThirdPartyDeliveryServiceCreate, 
    db: Session = Depends(get_db)
):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.ThirdPartyDeliveryService])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.ThirdPartyDeliveryService)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.ThirdPartyDeliveryService)
def update(
    item_id: int, 
    request: schema.ThirdPartyDeliveryServiceUpdate, 
    db: Session = Depends(get_db)
):
    return controller.update(db=db, item_id=item_id, request=request)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)