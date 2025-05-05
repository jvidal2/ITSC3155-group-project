from sqlalchemy.orm import Session
from ..models.order_tracking import OrderTracking
from ..schemas import order_tracking as schema

def create(db: Session, request: schema.OrderTrackingCreate):
    try:
        # Create new tracking record
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

def create(db: Session, request: schema.OrderTrackingCreate):
    try:
        # Create new tracking record
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