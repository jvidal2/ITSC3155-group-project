from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers import order_tracking as controller
from ..schemas import order_tracking as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Order Tracking'],
    prefix="/order-tracking"
)

@router.post("/", response_model=schema.OrderTracking, status_code=201)
def create(
    request: schema.OrderTrackingCreate, 
    db: Session = Depends(get_db)
):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.OrderTracking])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{order_id}", response_model=schema.OrderTracking)
def read_one(order_id: int, db: Session = Depends(get_db)):
    tracking = controller.read_one(db, order_id=order_id)
    if not tracking:
        raise HTTPException(status_code=404, detail="Order tracking not found.")
    return tracking

@router.put("/{order_id}", response_model=schema.OrderTracking)
def update(order_id: int, request: schema.OrderTrackingUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, order_id=order_id)