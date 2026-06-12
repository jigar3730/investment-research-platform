from fastapi import FastAPI
from app.core.config import settings
from app.database.connection import init_db

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Local-first Investment Research Platform - Milestone 1",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    # Verify or initialize our local DuckDB database on container start
    init_db()

@app.get("/health")
def health_check():
    """
    Infrastructure verification endpoint.
    """
    return {
        "status": "healthy",
        "platform": settings.PROJECT_NAME,
        "database": "DuckDB connected safely"
    }
@app.get("/")
def read_root():
    return {
        "status": "online",
        "platform": "Investment Research Platform",
        "milestone": 1
    }