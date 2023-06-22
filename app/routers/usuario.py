from fastapi import APIRouter, HTTPException
from app.data_base import usuarios, get_usuario
from app.models import Usuario, DatosUsuario

router = APIRouter()

@router.post("/register/")
async def crear_usuario(usuario: Usuario):
    username = usuario.username
    password = usuario.password
    email = usuario.email
    for u in usuarios.values():
        if u.username == username:
            raise HTTPException(status_code=400, detail="Ya existe un usuario con este nombre de usuario")
    
    # Asignar un ID al usuario
    user_id = len(usuarios) + 1
    nuevo_usuario = Usuario(id=user_id, username=username, password=password,email=email, carrito=[])
    
    # Agregar el nuevo usuario a la lista de usuarios
    usuarios[user_id] = nuevo_usuario
    
    return {"message": "Usuario creado exitosamente", "id": user_id}

@router.post("/login/")
async def login(usuario: Usuario):
    username = usuario.username
    password = usuario.password
    for id, u in usuarios.items():
        if u.username == username and u.password == password:
            return {"message": "Inicio de sesión exitoso", "id": u.id}
    raise HTTPException(status_code=401, detail="Usuario no encontrado")

@router.get("/usuarios/{id}")
async def obtener_usuario(id: int):
    if id in usuarios:
        return usuarios[id]
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
@router.get("/usuarios/{id}/carrito/")
async def obtener_carrito(id: int):
    if id not in usuarios:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # calcular el total del carrito
    total = sum([item.precio * item.cantidad for item in usuarios[id].carrito])
    
    # devolver el carrito junto con el total
    return {"carrito": usuarios[id].carrito, "total": total}

@router.put("/usuarios/{id}/datos-personales/")
async def actualizar_datos_personales(id: int, datos: DatosUsuario):
    if id not in usuarios:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Actualizar los datos personales del usuario
    usuarios[id].datos_personales = datos
    
    return usuarios[id]


@router.get("/usuarios/{id}/envio")
def obtener_estado_envio(id: int):
    usuario = get_usuario(id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Aquí puedes realizar la lógica para obtener el estado de envío real o simularlo
    # Puedes utilizar una API externa de seguimiento de envío o simular el estado de envío
    # según tus necesidades y requerimientos

    # Ejemplo de simulación de estado de envío
    estado_envio = "En tránsito"
    ubicacion = "Centro de distribución"

    return {"estado_envio": estado_envio, "ubicacion": ubicacion}