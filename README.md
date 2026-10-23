# Flask en Render

U2 · Actividad 5: práctica de despliegue continuo de una aplicación Flask en Render.

## Ejecutar localmente

Con Python 3, desde la carpeta del proyecto:

```sh
python -m venv .venv
```

Activa el entorno con `.venv\Scripts\Activate.ps1` en PowerShell o `source .venv/bin/activate` en macOS/Linux. Después:

```sh
python -m pip install -r requirements.txt
python app.py
```

Abre http://127.0.0.1:5000. La ruta `GET /` responde **API funcionando en Render**.

## Despliegue

[render.yaml](render.yaml) describe un servicio web de Python:

- Instalación: `pip install -r requirements.txt`.
- Arranque: `gunicorn app:app`.
- Disparador de despliegue automático: `commit`.

Conecta el repositorio a Render y revisa los registros de cada despliegue para comprobar su resultado. La configuración del repositorio no acredita por sí sola que exista un servicio publicado.

## Archivos

- [app.py](app.py): aplicación y ruta principal.
- [requirements.txt](requirements.txt): Flask y Gunicorn.
- [render.yaml](render.yaml): definición del servicio.

## Qué practico

Aplicaciones web mínimas, control de versiones y despliegue continuo.
