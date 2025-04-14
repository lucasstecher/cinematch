import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import relationship

from app.database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    title = Column(String, nullable=False)
    genres = Column(ARRAY(String))
    director = Column(String)
    actors = Column(ARRAY(String))

    watch_history = relationship(
        "WatchHistory", back_populates="movie", cascade="all, delete-orphan"
    )
    ratings = relationship(
        "Rating", back_populates="movie", cascade="all, delete-orphan"
    )
