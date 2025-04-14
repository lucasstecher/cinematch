from uuid import UUID

from sqlalchemy.orm import Session

from app.models.movie import Movie


def get_all_movies(db: Session) -> list[Movie]:
    return db.query(Movie).all()


def get_movie_by_id(db: Session, movie_id: UUID) -> Movie | None:
    return db.query(Movie).filter(Movie.id == movie_id).first()


def create_movie(
    db: Session, title: str, genres: list[str], director: str, actors: list[str]
) -> Movie:
    movie = Movie(title=title, genres=genres, director=director, actors=actors)
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie
