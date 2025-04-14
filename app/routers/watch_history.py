from uuid import UUID

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.controllers import watch_history
from app.database import get_db

router = APIRouter()


class WatchRequest(BaseModel):
    user_id: UUID


@router.post("/movies/{movie_id}/watch")
def watch_movie(movie_id: UUID, data: WatchRequest, db: Session = Depends(get_db)):
    return watch_history.log_watch(data.user_id, movie_id, db)
