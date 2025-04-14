from uuid import UUID

from sqlalchemy.orm import Session

from app.models.rating import Rating


def create_or_update_rating(
    db: Session, user_id: UUID, movie_id: UUID, score: float
) -> Rating:
    rating = db.query(Rating).filter_by(user_id=user_id, movie_id=movie_id).first()
    if rating:
        rating.score = score
    else:
        rating = Rating(user_id=user_id, movie_id=movie_id, score=score)
        db.add(rating)

    db.commit()
    db.refresh(rating)
    return rating


def get_user_ratings(db: Session, user_id: UUID) -> list[Rating]:
    return db.query(Rating).filter_by(user_id=user_id).all()
