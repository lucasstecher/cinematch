from uuid import UUID

from sqlalchemy.orm import Session

from app.repositories import watch_history


def log_movie_watch(db: Session, user_id: UUID, movie_id: UUID):
    return watch_history.log_watch(db, user_id, movie_id)


def get_watched_movie_ids(db: Session, user_id: UUID):
    return watch_history.get_watched_movies_ids(db, user_id)
