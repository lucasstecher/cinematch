from uuid import UUID

from sqlalchemy.orm import Session

from app.services import movie


def list_movies(db: Session):
    return movie.list_all_movies(db)


def get_movie_by_id(movie_id: UUID, db: Session):
    return movie.get_movie(db, movie_id)
