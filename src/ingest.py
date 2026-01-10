"""Data ingestion helpers: CSV loader and SQL query helper."""
from typing import Optional
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()


def load_csv(path: str) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(path)


def query_sql(query: str, connection_string: Optional[str] = None) -> pd.DataFrame:
    """Run a SQL query and return a DataFrame.

    Provide `connection_string` or set `DATABASE_URL` in env.
    """
    conn = connection_string or os.getenv("DATABASE_URL")
    if not conn:
        raise ValueError("No database connection string provided. Set DATABASE_URL or pass connection_string.")
    engine = create_engine(conn)
    with engine.connect() as connection:
        df = pd.read_sql_query(query, connection)
    return df
