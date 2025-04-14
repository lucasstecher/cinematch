from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.watch_history import WatchHistory


def log_watch(db: Session, user_id: UUID, movie_id: UUID) -> WatchHistory:
    watch = WatchHistory(
        user_id=user_id, movie_id=movie_id, watched_at=datetime.utcnow()
    )
    db.add(watch)
    db.commit()
    db.refresh(watch)
    return watch


def get_watched_movies_ids(db: Session, user_id: UUID) -> list[UUID]:
    return [
        row.movie_id for row in db.query(WatchHistory).filter_by(user_id=user_id).all()
    ]
