from uuid import UUID

from sqlalchemy.orm import Session

from app.repositories import rating


def rate_movie(db: Session, user_id: UUID, movie_id: UUID, score: float):
    return rating.create_or_update_rating(db, user_id, movie_id, score)
