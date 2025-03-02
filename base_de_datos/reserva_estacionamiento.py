from async_easy_model import EasyModel,db_config,init_db
from sqlmodel import Relationship,Field
from typing import List, Optional
from pydantic import EmailStr
from datetime import datetime


db_config.configure_sqlite('base_de_datos/reservas_estacionamiento.db')

class Usuarios(EasyModel, table=True):
    """
    Registro de usuarios 
    """
    id: Optional[int] = Field(default=None, primary_key=True, index=True) # pagina a enviar
    nombre: str = Field(...,min_length=1, description="Nombre del Usuario")
    apellido: str = Field(...,min_length=1, description="Apellido del Usuario")
    rut: str = Field(..., min_length=8, max_length=9, description="RUT sin puntos ni guion") #
    email: EmailStr = Field(...,min_length=1, description="Correo del Usuario") #valida el correo
    telefono: str = Field(...,min_length=9, description="Telefono del Usuario")
    contrasena: str = Field(...,min_length=8, description="Contraseña del Usuario")
    
class Vehiculos(EasyModel, table=True):
    """
    Registro de vehiculos
    """
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    marca: str = Field(...,min_length=1, description="Marca del Vehiculo")
    modelo: str = Field(...,min_length=1, description="Modelo del Vehiculo")
    patente: str = Field(...,min_length=1, description="Patente del Vehiculo")
    color: str = Field(...,min_length=1, description="Color del Vehiculo")
    id_usuario: Optional[int] = Field(default=None, foreign_key="usuarios.id",description="Dueño del vehiculo")

class Discapacitado(EasyModel, table=True):

    __tablename__ = "discapacitados"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    id_usuario: Optional[int] = Field(default=None, foreign_key="usuarios.id")
    folio: str = Field(...,min_length=10,description="Folio para personas discapacitadas")

  
class Horarios(EasyModel, table=True):
    """
    Horarios de disponibilidad
    """
    id: Optional[int] = Field(default=None, primary_key=True, index=True) 
    dia_semana: str = Field(..., description="Día de la semana")
    hora: str = Field(..., description="Hora específica")
    semana: int = Field(..., description="Número de la semana en el año")
    mes: str = Field(..., description="Mes del año")


class Estacionamientos(EasyModel, table=True):
    """
    Estacionamientos que estaran disponibles
    """
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    ubicacion: str = Field(..., description="Ubicación")
    capacidad: int = Field(..., description=" espacios disponibles")
    precio_hora: float = Field(..., description="Precio por hora")
    precio_dia: float = Field(..., description="Precio por día")
    precio_semana: float = Field(..., description="Precio por semana")
    precio_mes: float = Field(..., description="Precio por mes")
    #precios por rango de fechas(para temporadas altas bajas)
class Reserva(EasyModel, table=True):
    """
    Reservas para los estacionamientos
    """
    __tablename__ = "reservas"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    id_usuario: Optional[int] = Field(default=None, foreign_key="usuarios.id")
    id_vehiculo: Optional[int] = Field(default=None, foreign_key="vehiculos.id")
    id_estacionamiento: Optional[int] = Field(default=None, foreign_key="estacionamientos.id")
    fecha_inicio: datetime = Field(..., description=" inicio de la reserva")
    fecha_fin: datetime = Field(..., description=" término de la reserva")
    estado: str = Field(..., description="Estado de la reserva (activa, cancelada, finalizada)")

class Pagos(EasyModel, table=True):
    """
    Registro de transacciones de pago
    """
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    id_usuario: Optional[int] = Field(default=None, foreign_key="usuarios.id")
    id_reserva: Optional[int] = Field(default=None, foreign_key="reservas.id")
    monto: float = Field(..., description="Monto del pago")
    metodo_pago: str = Field(..., description="Método de pago (tarjeta, efectivo, etc.)")
    fecha_pago: datetime = Field(default_factory=datetime.utcnow, description="Fecha del pago")
    estado: str = Field(..., description="Estado del pago (completado, pendiente, fallido)")

class TarifasEspeciales(EasyModel, table=True):
    """
    Tarifas especiales para temporadas altas o descuentos
    """
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    descripcion: str = Field(..., description="Descripción de la tarifa especial")
    porcentaje_descuento: float = Field(..., description="Porcentaje de descuento aplicado")
    fecha_inicio: datetime = Field(..., description="Inicio de la tarifa especial")
    fecha_fin: datetime = Field(..., description="Fin de la tarifa especial")
