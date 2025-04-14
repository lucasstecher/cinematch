from typing import List
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.user import User
from app.services import user


def get_all_users(db: Session) -> List[User]:
    return user.list_users(db)


def get_user(user_id: UUID, db: Session):
    return user.get_user_by_id(db, user_id)


def create_user(name: str, db: Session):
    return user.create_user(db, name)
