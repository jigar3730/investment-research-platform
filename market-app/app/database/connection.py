import duckdb
from contextlib import contextmanager
from app.core.config import settings
import os

# Ensure data directory exists locally
os.makedirs(os.path.dirname(settings.DATABASE_PATH), exist_ok=True)

@contextmanager
def get_db_connection():
    """
    Context manager to safely open and close a DuckDB connection.
    DuckDB allows multiple readers but only one writer at a time.
    """
    conn = duckdb.connect(database=settings.DATABASE_PATH, read_only=False)
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    """
    Initializes basic health check or verification structures if needed.
    Future migrations/schema creation can be invoked here.
    """
    with get_db_connection() as conn:
        # Simple verification query
        conn.execute("SELECT 1;")