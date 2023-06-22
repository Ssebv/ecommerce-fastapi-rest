from pydantic import BaseModel
from typing import List, Optional

class Producto(BaseModel):
    id: int
    nombre: str
    stock: int
    precio: float

class CarritoItemIn(BaseModel):  
    nombre: str
    cantidad: int

class CarritoItemOut(BaseModel):
    id: int
    nombre: str
    cantidad: int
    precio: float
    
class HistorialCompra(BaseModel):
    id: int
    producto: str
    cantidad: int
    total: float
    
class DatosUsuario(BaseModel):
    direccion: str
    telefono: str

class Usuario(BaseModel):
    username: str
    password: str
    email: Optional[str] = None
    id: Optional[int] = None 
    carrito: List[CarritoItemOut] = []
    historial_compras: List[HistorialCompra] = []  # Campo para el historial de compras
    datos_personales: Optional[DatosUsuario] = None
    

class Pago(BaseModel):
    id: int
    usuario_id: int
    total: float
    estado: str