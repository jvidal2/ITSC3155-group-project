from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from sqlalchemy.exc import SQLAlchemyError
from ..models.order_tracking import OrderTracking
from ..schemas import order_tracking as schema

def create(db: Session, request: schema.OrderTrackingCreate):
    try:
        tracking = OrderTracking(
            order_id=request.order_id,
            status=request.status
        )
        
        db.add(tracking)
        db.commit()
        db.refresh(tracking)
        return tracking
        
    except SQLAlchemyError as e:
        db.rollback()
        error = str(getattr(e, "orig", e))
        raise HTTPException(status_code=400, detail=error)
    
def read_all(db: Session):
    return db.query(OrderTracking).all()

def read_one(db: Session, order_id: int):
    return db.query(OrderTracking).filter(OrderTracking.order_id == order_id).first()

def update(db: Session, request: schema.OrderTrackingUpdate, order_id: int):
    tracking = db.query(OrderTracking).filter(OrderTracking.order_id == order_id).first()
    if not tracking:
        return None
    for field, value in request.dict(exclude_unset=True).items():
        setattr(tracking, field, value)
    db.commit()
    db.refresh(tracking)
    return tracking

def delete(db: Session, order_id: int):
    try:
        item = db.query(OrderTracking).filter(OrderTracking.order_id == order_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order tracking not found")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)