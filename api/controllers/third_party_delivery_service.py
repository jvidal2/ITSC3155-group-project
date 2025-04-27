from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import third_party_delivery_service as model
from ..schemas import third_party_delivery_service as schema
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.ThirdPartyDeliveryService(
        name=request.name,
        amount=request.amount,
        status=request.status
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return schema.ThirdPartyDeliveryService.from_orm(new_item)


def read_all(db: Session):
    try:
        result = db.query(model.ThirdPartyDeliveryService).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return [schema.ThirdPartyDeliveryService.from_orm(item) for item in result]


def read_one(db: Session, item_id):
    try:
        item = db.query(model.ThirdPartyDeliveryService).filter(model.ThirdPartyDeliveryService.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return schema.ThirdPartyDeliveryService.from_orm(item)


def update(db: Session, item_id, request):
    try:
        item = db.query(model.ThirdPartyDeliveryService).filter(model.ThirdPartyDeliveryService.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    updated_item = item.first()
    return schema.ThirdPartyDeliveryService.from_orm(updated_item)


def delete(db: Session, item_id):
    try:
        item = db.query(model.ThirdPartyDeliveryService).filter(model.ThirdPartyDeliveryService.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)