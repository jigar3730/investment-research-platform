import duckdb
import os
import logging

# Configure logging to match Uvicorn's stream
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_PATH = "/app/data/platform.db"
SCHEMA_PATH = "/app/app/database/schema.sql"

def get_db_connection():
    """Returns a connection to the local DuckDB instance."""
    return duckdb.connect(database=DB_PATH, read_only=False)

def init_db():
    """Reads and executes the schema.sql file to initialize tables."""
    logger.info("Starting database initialization...")
    
    if os.path.exists(SCHEMA_PATH):
        try:
            with open(SCHEMA_PATH, 'r') as f:
                schema_sql = f.read()
            
            with get_db_connection() as conn:
                conn.execute(schema_sql)
                logger.info("Database initialized and seed data ingested successfully.")
        except Exception as e:
            logger.error(f"CRITICAL ERROR during DuckDB execution: {e}")
    else:
        logger.warning(f"Schema file not found at {SCHEMA_PATH}")
