import os
from nicegui_router import Server
from pathlib import Path
import asyncio
from async_easy_model import init_db  # Asegúrate de importar init_db desde el archivo correcto
from db_config import configure_sqlite  # Asegúrate de importar configure_sqlite

# Asegurarse de que el directorio de la base de datos exista
DB_PATH = 'base_de_datos/reservas_estacionamiento.db'

# Verificar si la base de datos ya existe
if os.path.exists(DB_PATH):
    print(f"La base de datos ya existe en: {DB_PATH}")
else:
    print(f"La base de datos no existe. Intentando crearla en: {DB_PATH}")

# Crear directorio si no existe
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

async def startup_db_reservas_estacionamiento():
    """Inicializa la base de datos en el arranque del servidor."""
    try:
        engine = configure_sqlite(DB_PATH)  # Configura el engine
        print(f"Engine configurado con DB_PATH: {DB_PATH}")
        
        # Verificar si el engine se inicializa correctamente
        if engine:
            print("Engine creado correctamente.")
        
        # Crear la base de datos
        await init_db(engine)  # Llamamos a init_db pasándole el engine
        print(f"Base de datos creada correctamente en: {DB_PATH}")

        # Verificar si el archivo de la base de datos realmente existe ahora
        if os.path.exists(DB_PATH):
            print(f"El archivo de la base de datos se ha creado en: {DB_PATH}")
        else:
            print(f"El archivo de la base de datos NO se ha creado.")
    except Exception as e:
        print(f"Error al crear la base de datos: {e}")

server_instance = Server(
    title="Reserva de Estacionamientos",
    routes_dir=Path(__file__).parent / "paginas",  # Verifica que esté correcto
    on_startup=lambda: asyncio.create_task(startup_db_reservas_estacionamiento()),  # Corre la tarea asíncrona
    ui={"language": "es"}
)

# Verifica las rutas registradas
print("Rutas registradas:")
for route in server_instance.app.router.routes:
    print(route)

app = server_instance.app

if __name__ == '__main__':
    server_instance.listen(port=8080)
