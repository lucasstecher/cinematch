from uuid import UUID

from sqlalchemy.orm import Session

from app.repositories import movie


def list_all_movies(db: Session):
    return movie.get_all_movies(db)


def get_movie(db: Session, movie_id: UUID):
    return movie.get_movie_by_id(db, movie_id)
