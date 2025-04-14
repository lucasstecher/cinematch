from fastapi import FastAPI

from app.routers import movie, rating, recommendation, user, watch_history

app = FastAPI()

app.include_router(user.router)
app.include_router(movie.router)
app.include_router(rating.router)
app.include_router(watch_history.router)
app.include_router(recommendation.router)
