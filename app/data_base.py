from typing import List
from app.models import Producto, Pago

usuarios = {}

pagos: List[Pago] = []   # Agrega esta línea
historial_compras: List[Pago] = []  # Agrega esta línea para el historial de compras

productos_base: List[Producto] = [
    Producto(id=1, nombre="Producto 1", stock=10, precio=10.0),
    Producto(id=2, nombre="Producto 2", stock=5, precio=20.0),
    Producto(id=3, nombre="Producto 3", stock=8, precio=15.0),
]

def get_usuario(id: int):
    return usuarios.get(id)

def get_producto(id: int):
    for producto in productos_base:
        if producto.id == id:
            return producto
    return None

def buscar_producto_por_nombre(nombre: str):
    for producto in productos_base:
        if producto.nombre == nombre:
            return producto
    return None