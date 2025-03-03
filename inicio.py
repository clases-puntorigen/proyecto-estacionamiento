from nicegui_router import Server   #importa el servidor para rutas
from pathlib import Path  #para rutas de archivos
import asyncio
from async_easy_model import init_db, db_config


async def startup_db_reservas_estacionamiento():
    await init_db()
    print("base de datos creada")

# servidor
server_instance = Server(
    title="Reserva de Estacionamientos",
    routes_dir=Path(__file__).parent / "paginas",
    on_startup=startup_db_reservas_estacionamiento,
    ui={
        "language": "es"
    }
)

app = server_instance.app

if __name__ == '__main__':
    server_instance.listen(port=8080)
