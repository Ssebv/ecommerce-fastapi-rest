from fastapi import APIRouter, HTTPException
from app.models import CarritoItemIn, CarritoItemOut 
from app.data_base import buscar_producto_por_nombre, get_usuario



router = APIRouter()

# Agrega al carrito un producto
@router.post("/usuarios/{usuario_id}/carrito/agregar")
def agregar_producto_carrito(usuario_id: int, item: CarritoItemIn):
    usuario = get_usuario(usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    producto_base = buscar_producto_por_nombre(item.nombre)
    if producto_base is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    if item.cantidad > producto_base.stock:
        raise HTTPException(status_code=400, detail="Cantidad solicitada no disponible")

    item_carrito = CarritoItemOut(
        id=producto_base.id,
        nombre=producto_base.nombre,
        cantidad=item.cantidad,
        precio=producto_base.precio,
      
    )

    usuario.carrito.append(item_carrito)
    return {"message": "Producto añadido al carrito"}

# Elimina un producto del carrito
@router.delete("/usuarios/{id}/carrito/eliminar")
async def eliminar_producto_carrito(id: int, item: CarritoItemIn):

    
    usuario = get_usuario(id)
    
    for item_carrito in usuario.carrito:
        if item_carrito.nombre == item.nombre:
            if item.cantidad <= item_carrito.cantidad:
                item_carrito.cantidad -= item.cantidad
                if item_carrito.cantidad == 0:
                    usuario.carrito.remove(item_carrito)
                return {"message": f"Se eliminaron {item.cantidad} unidades del producto {item.nombre}"}
            else:
                raise HTTPException(status_code=400, detail="Cantidad a eliminar supera la cantidad en el carrito")
    
    raise HTTPException(status_code=404, detail="Producto no encontrado en el carrito")