from fastapi import APIRouter, HTTPException
from app.models import Pago
from app import data_base as db
from app.data_base import get_usuario

# Agrega aquí la función para simular el envío de correo
def enviar_correo(destinatario, asunto, mensaje):
    print("Enviando correo...")
    print(f"Destinatario: {destinatario}")
    print(f"Asunto: {asunto}")
    print(f"Mensaje: {mensaje}")
    print("Correo enviado")

router = APIRouter()

@router.post("/usuarios/{usuario_id}/pagar")
def realizar_pago(usuario_id: int):
    usuario = get_usuario(usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if not usuario.carrito:
        raise HTTPException(status_code=400, detail="El carrito está vacío. No se puede realizar el pago.")

    total_carrito = sum([item.cantidad * item.precio for item in usuario.carrito])

    pago = Pago(id=len(db.pagos) + 1, usuario_id=usuario_id, total=total_carrito, estado="Pagado")
    db.pagos.append(pago)
    db.historial_compras.append(pago)  # Agrega el pago al historial de compras

    # Vaciamos el carrito después del pago
    usuario.carrito = []

    # Simulación de envío de correo
    enviar_correo(usuario.email, "Compra exitosa", f"¡Gracias por tu compra! El total pagado es: {total_carrito}. Tu producto llegará en 3 días hábiles.")

    return {"message": "Pago realizado exitosamente", "pago": pago}


@router.get("/usuarios/{usuario_id}/historial")
def obtener_historial_compras(usuario_id: int):
    usuario = get_usuario(usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    historial = [pago for pago in db.historial_compras if pago.usuario_id == usuario_id]
    return {"historial": historial}