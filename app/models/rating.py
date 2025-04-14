import uuid

from sqlalchemy import Column, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    movie_id = Column(UUID(as_uuid=True), ForeignKey("movies.id"))
    score = Column(Float)

    user = relationship("User", back_populates="ratings")
    movie = relationship("Movie", back_populates="ratings")
