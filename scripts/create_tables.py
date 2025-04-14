import os
import sys

from app.database import Base, engine
# noqa: F401
from app.models import movie, rating, user, watch_history  # noqa: F401

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def create_tables():
    print("Creating tables in the database...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")


if __name__ == "__main__":
    create_tables()
