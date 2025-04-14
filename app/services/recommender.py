from uuid import UUID

from sqlalchemy.orm import Session

from app.repositories import movie, rating, watch_history
from app.utils.preferences import get_favorite_actors, get_favorite_directors


def recommend_movies_for_user(db: Session, user_id: UUID, top_n: int = 5):
    ratings = rating.get_user_ratings(db, user_id)

    liked_movies = [rating.movie for rating in ratings if rating.score >= 4.0]

    if not liked_movies:
        return []

    all_movies = movie.get_all_movies(db)
    watched_ids = set(watch_history.get_watched_movies_ids(db, user_id))

    candidate_movies = [m for m in all_movies if m.id not in watched_ids]

    if not candidate_movies:
        return []

    favorite_directors = get_favorite_directors(liked_movies)
    favorite_actors = get_favorite_actors(liked_movies)

    scored_movies = []

    for m in candidate_movies:
        score = 0
        if m.director in favorite_directors:
            score += 1
        if any(actor in favorite_actors for actor in (m.actors or [])):
            score += 1
        if any(
            genre in [g for lm in liked_movies for g in (lm.genres or [])]
            for genre in (m.genres or [])
        ):
            score += 1
        scored_movies.append((m, score))

    scored_movies.sort(key=lambda x: x[1], reverse=True)
    return [movie for movie, _ in scored_movies[:top_n]]
