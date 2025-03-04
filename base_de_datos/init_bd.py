from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Esta es tu función init_db que toma el engine como argumento
async def init_db(engine):
    """Inicializa la base de datos creando las tablas."""
    try:
        print("Iniciando la creación de la base de datos...")
        
        # Crea las tablas (si no existen)
        Base.metadata.create_all(bind=engine)
        print("Base de datos creada correctamente.")
    except Exception as e:
        print(f"Error al crear la base de datos: {e}")
