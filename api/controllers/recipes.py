from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import recipes as model
from ..schemas import recipes as schema
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request: schema.RecipeCreate):
    new_recipe = model.Recipe(
        sandwich_id=request.sandwich_id,
        resource_id=request.resource_id,
        amount=request.amount
    )

    try:
        db.add(new_recipe)
        db.commit()
        db.refresh(new_recipe)
        return new_recipe
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def read_all(db: Session):
    try:
        return db.query(model.Recipe).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def read_one(db: Session, item_id: int):
    try:
        recipe = db.query(model.Recipe).filter(model.Recipe.id == item_id).first()
        if not recipe:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
        return recipe
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def update(db: Session, item_id: int, request: schema.RecipeUpdate):
    try:
        recipe = db.query(model.Recipe).filter(model.Recipe.id == item_id)
        if not recipe.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
        recipe.update(request.model_dump(exclude_unset=True), synchronize_session=False)
        db.commit()
        return recipe.first()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def delete(db: Session, item_id: int):
    try:
        recipe = db.query(model.Recipe).filter(model.Recipe.id == item_id)
        if not recipe.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
        recipe.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
