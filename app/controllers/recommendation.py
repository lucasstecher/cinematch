from uuid import UUID

from sqlalchemy.orm import Session

from app.services import recommender


def get_recommendations(user_id: UUID, db: Session):
    return recommender.recommend_movies_for_user(db, user_id)
