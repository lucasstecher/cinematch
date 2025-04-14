from uuid import UUID

from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories import user


def list_users(db: Session):
    return user.get_all_users(db)


def get_user_by_id(db: Session, user_id: UUID) -> User | None:
    return user.get_user_by_id(db, user_id)


def create_user(db: Session, name: str) -> User:
    return user.create_user(db, name)
