from collections import Counter

from app.models.movie import Movie


def get_favorite_directors(movies: list[Movie], top_n=3) -> list[str]:
    directors = [movie.director for movie in movies if movie.director]
    counter = Counter(directors)
    return [d for d, _ in counter.most_common(top_n)]


def get_favorite_actors(movies: list[Movie], top_n=5) -> list[str]:
    all_actors = []
    for movie in movies:
        all_actors.extend(movie.actors or [])
    counter = Counter(all_actors)
    return [a for a, _ in counter.most_common(top_n)]
