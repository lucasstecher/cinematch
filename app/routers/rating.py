from uuid import UUID

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.controllers import rating
from app.database import get_db

router = APIRouter()


class RatingRequest(BaseModel):
    user_id: UUID
    movie_id: UUID
    score: float


@router.post("/ratings")
def rate_movie(data: RatingRequest, db: Session = Depends(get_db)):
    return rating.rate_movie(data.user_id, data.movie_id, data.score, db)
