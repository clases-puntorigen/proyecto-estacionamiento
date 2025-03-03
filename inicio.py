from nicegui_router import Server  # importa el servidor para rutas
from pathlib import Path  # para rutas de archivos
import asyncio
from async_easy_model import init_db  # Importa la función init_db
from db_config import configure_sqlite  # importa la configuración del engine

def startup_db_reservas_estacionamiento():
    engine = configure_sqlite('base_de_datos/reservas_estacionamiento.db')
    asyncio.create_task(init_db(engine))  # Usamos create_task para correr la tarea asíncrona
    print("Base de datos creada correctamente")

server_instance = Server(
    title="Reserva de Estacionamientos",
    routes_dir=Path(__file__).parent / "paginas",  # Verifica que esté correcto
    on_startup=startup_db_reservas_estacionamiento,
    ui={"language": "es"}
)

# Verifica las rutas registradas
print("Rutas registradas:")
for route in server_instance.app.router.routes:
    print(route)

app = server_instance.app

if __name__ == '__main__':
    server_instance.listen(port=8080)
