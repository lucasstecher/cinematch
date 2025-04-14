import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    name = Column(String, nullable=False)

    watch_history = relationship(
        "WatchHistory", back_populates="user", cascade="all, delete-orphan"
    )
    ratings = relationship(
        "Rating", back_populates="user", cascade="all, delete-orphan"
    )
