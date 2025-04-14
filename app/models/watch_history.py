import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class WatchHistory(Base):
    __tablename__ = "watch_history"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    movie_id = Column(UUID(as_uuid=True), ForeignKey("movies.id"))
    watched_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="watch_history")
    movie = relationship("Movie", back_populates="watch_history")
