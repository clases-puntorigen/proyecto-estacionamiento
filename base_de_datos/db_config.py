from sqlalchemy import create_engine

def configure_sqlite(db_path):
    DATABASE_URL = f"sqlite:///{db_path}"
    return create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
