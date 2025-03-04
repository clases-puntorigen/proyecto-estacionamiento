from sqlalchemy import create_engine

def configure_sqlite(db_path):
    """Configura y retorna el engine para SQLite."""
    engine = create_engine(f"sqlite:///{db_path}")
    return engine
