from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers import user
from app.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def list_users(db: Session = Depends(get_db)):
    return user.get_all_users(db)


@router.get("/{user_id}")
def get_user(user_id: UUID, db: Session = Depends(get_db)):
    return user.get_user(user_id, db)


@router.post("/")
def create_user(name: str, db: Session = Depends(get_db)):
    return user.create_user(name, db)
