import os
import sys
from uuid import uuid4

from app.database import SessionLocal
from app.models import movie, rating, user, watch_history

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def seed_data():
    db = SessionLocal()
    print("🌱 Inserindo dados fake no banco...")

    existing_users = db.query(user.User).count()
    if existing_users > 0:
        print("⚠️ Seed ignorado: já existem dados no banco.")
        db.close()
        return

    u = user.User(id=uuid4(), name="Teste")
    db.add(u)
    db.commit()

    filmes = [
        movie.Movie(
            id=uuid4(),
            title="A Origem",
            genres=["Ação", "Ficção Científica"],
            director="Christopher Nolan",
            actors=["Leonardo DiCaprio", "Tom Hardy"],
        ),
        movie.Movie(
            id=uuid4(),
            title="Clube da Luta",
            genres=["Drama", "Suspense"],
            director="David Fincher",
            actors=["Brad Pitt", "Edward Norton"],
        ),
        movie.Movie(
            id=uuid4(),
            title="O Grande Truque",
            genres=["Drama", "Mistério"],
            director="Christopher Nolan",
            actors=["Hugh Jackman", "Christian Bale"],
        ),
        movie.Movie(
            id=uuid4(),
            title="O Lobo de Wall Street",
            genres=["Comédia", "Drama"],
            director="Martin Scorsese",
            actors=["Leonardo DiCaprio", "Jonah Hill"],
        ),
    ]

    db.add_all(filmes)
    db.commit()

    views = [
        watch_history.WatchHistory(id=uuid4(), user_id=u.id, movie_id=filmes[0].id),
        watch_history.WatchHistory(id=uuid4(), user_id=u.id, movie_id=filmes[1].id),
    ]
    db.add_all(views)
    db.commit()

    ratings = [
        rating.Rating(id=uuid4(), user_id=u.id, movie_id=filmes[0].id, score=4.5),
        rating.Rating(id=uuid4(), user_id=u.id, movie_id=filmes[1].id, score=4.0),
    ]
    db.add_all(ratings)
    db.commit()

    db.close()
    print("✅ Seed finalizado com sucesso.")


if __name__ == "__main__":
    seed_data()
