from fastapi import FastAPI
from app.routers import carrito, usuario, pago

app = FastAPI()

app.include_router(carrito.router)
app.include_router(usuario.router)
app.include_router(pago.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

