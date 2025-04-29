from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import user as model
from ..schemas import user as schema
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request: schema.UserCreate):
    new_user = model.User(
        name=request.name,
        email=request.email,
        phone_number=request.phone_number
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except SQLAlchemyError as e:
        error = str(getattr(e, "orig", e))
        raise HTTPException(status_code=500, detail=error)


def read_all(db: Session):
    try:
        return db.query(model.User).all()
    except SQLAlchemyError as e:
        error = str(getattr(e, "orig", e))
        raise HTTPException(status_code=500, detail=error)


def read_one(db: Session, item_id: int):
    try:
        user = db.query(model.User).filter(model.User.user_id == item_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user
    except SQLAlchemyError as e:
        error = str(getattr(e, "orig", e))
        raise HTTPException(status_code=500, detail=error)


def update(db: Session, item_id: int, request: schema.UserUpdate):
    try:
        user = db.query(model.User).filter(model.User.user_id == item_id)
        if not user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        user.update(request.model_dump(exclude_unset=True), synchronize_session=False)
        db.commit()
        return user.first()
    except SQLAlchemyError as e:
        error = str(getattr(e, "orig", e))
        raise HTTPException(status_code=500, detail=error)


def delete(db: Session, item_id: int):
    try:
        user = db.query(model.User).filter(model.User.user_id == item_id)
        if not user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        user.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        error = str(getattr(e, "orig", e))
        raise HTTPException(status_code=500, detail=error)