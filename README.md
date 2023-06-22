

# Documentación del Proyecto

Esta documentación proporciona los pasos necesarios para instalar y configurar el proyecto correctamente.

## Descripción del Proyecto

El objetivo de este proyecto es desarrollar una API robusta y eficiente para un sistema de comercio electrónico. La API permite a los usuarios registrar una cuenta, agregar productos al carrito, realizar pagos, ver el historial de compras y realizar un seguimiento de envío de los productos adquiridos

## Requisitos Previos

Antes de comenzar, asegúrate de tener lo siguiente instalado en tu sistema:

- Python 3.11
- Pipenv (si no lo tienes instalado, sigue las instrucciones en [https://pipenv.pypa.io/en/latest/install/](https://pipenv.pypa.io/en/latest/install/) para instalarlo)
- Visual Studio Code (opcional)

## Pasos de Instalación

1. Navega hasta la carpeta del proyecto.
   
```shell
cd /Proyecto
```
2. Crea un entorno virtual y activa el entorno virtual usando Pipenv.

```shell
pipenv shell
```

Esto creará un entorno virtual e instalará automáticamente todas las dependencias del proyecto.

3. Instala las dependencias utilizando el archivo `requirements.txt`.

```shell
pipenv install -r requirements.txt
```
Esto instalará las dependencias del proyecto utilizando el archivo `requirements.txt`.

4. Ejecuta el servidor de desarrollo dentro de la carpeta Proyecto/app

```shell
uvicorn main:app --reload
```
El servidor de desarrollo se ejecutará en `http://localhost:8000`. Puedes acceder a la API y probarla en tu navegador o mediante herramientas como Postman.

Con estos pasos, habrás instalado el proyecto y estarás listo para comenzar a trabajar con él.

5. Uso del archivo test.rest
   
El archivo test.rest es un archivo de texto plano que contiene solicitudes HTTP para probar la API. Para utilizarlo, se recomienda tener instalada la extensión "REST Client" en Visual Studio Code. Esta extensión permite enviar solicitudes HTTP directamente desde el IDE y ver las respuestas.

A continuación se muestra cómo utilizar el archivo test.rest:

   - Abre el archivo test.rest en Visual Studio Code despues de haber instalado [Rest Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)

   - Haz clic en el botón "Send Request" junto a una solicitud para ejecutarla. La solicitud se enviará a la API y la respuesta se mostrará en el panel de resultados.

Observa la respuesta obtenida y verifica el funcionamiento correcto de la API.

Repite estos pasos para realizar diferentes solicitudes y probar diferentes funcionalidades de la API.

6. Estructura de archivos

```shell
.
├── Proyecto
│   ├── app
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── routers
│   │       ├── __init__.py
│   │       ├── carrito.py
│   │       ├── pago.py
│   │       ├── usuario.py
│   │       └── envio.py
│   ├── tests
│   │   ├── __init__.py
│   │   └── test_api.py
│   ├── Pipfile
│   ├── Pipfile.lock
│   ├── requirements.txt
│   ├── test.rest
│   └── README.md
└──
```

