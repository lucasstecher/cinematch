from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers import movie
from app.database import get_db

router = APIRouter()


@router.get("/movies")
def list_movies(db: Session = Depends(get_db)):
    return movie.list_movies(db)


@router.get("/movies/{movie_id}")
def get_movie(movie_id: UUID, db: Session = Depends(get_db)):
    return movie.get_movie_by_id(movie_id, db)
