from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers import recommendation
from app.database import get_db

router = APIRouter()


@router.get("/movies/{user_id}/recommendations")
def get_recommendations(user_id: UUID, db: Session = Depends(get_db)):
    return recommendation.get_recommendations(user_id, db)
