from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import sandwiches as model
from ..schemas import sandwiches as schema
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request: schema.SandwichCreate):
    new_sandwich = model.Sandwich(
        sandwich_name=request.sandwich_name,
        price=request.price
    )

    try:
        db.add(new_sandwich)
        db.commit()
        db.refresh(new_sandwich)
        return new_sandwich
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def read_all(db: Session):
    try:
        return db.query(model.Sandwich).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def read_one(db: Session, item_id: int):
    try:
        sandwich = db.query(model.Sandwich).filter(model.Sandwich.id == item_id).first()
        if not sandwich:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")
        return sandwich
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def update(db: Session, item_id: int, request: schema.SandwichUpdate):
    try:
        sandwich = db.query(model.Sandwich).filter(model.Sandwich.id == item_id)
        if not sandwich.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")
        sandwich.update(request.model_dump(exclude_unset=True), synchronize_session=False)
        db.commit()
        return sandwich.first()
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def delete(db: Session, item_id: int):
    try:
        sandwich = db.query(model.Sandwich).filter(model.Sandwich.id == item_id)
        if not sandwich.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")
        sandwich.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
