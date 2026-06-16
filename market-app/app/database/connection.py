import logging
import os
from contextlib import contextmanager

import duckdb

from app.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")

os.makedirs(os.path.dirname(settings.DATABASE_PATH), exist_ok=True)


@contextmanager
def get_db_connection():
    """Returns a context-managed connection to the local DuckDB instance."""
    conn = duckdb.connect(database=settings.DATABASE_PATH, read_only=False)
    try:
        yield conn
    finally:
        conn.close()


def init_db():
    """Reads and executes schema.sql to initialize tables and seed data."""
    logger.info("Starting database initialization...")

    if not os.path.exists(SCHEMA_PATH):
        logger.warning(f"Schema file not found at {SCHEMA_PATH}")
        return

    try:
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            schema_sql = f.read()

        with get_db_connection() as conn:
            conn.execute(schema_sql)
            logger.info("Database initialized and seed data ingested successfully.")
    except Exception as e:
        logger.error(f"CRITICAL ERROR during DuckDB execution: {e}")
