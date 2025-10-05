from sqlalchemy import create_engine
import os

def get_engine():
    user = os.getenv("POSTGRES_USER", "admin")
    password = os.getenv("POSTGRES_PASSWORD", "admin123")
    host = os.getenv("POSTGRES_HOST", "postgres_db")
    port = os.getenv("POSTGRES_PORT", "5432")
    db = os.getenv("POSTGRES_DB", "analytics_db")
    
    return create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
