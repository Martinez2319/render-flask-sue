# U2 Actividad 7 Proyecto Deploy con Docker

Aplicación Flask empaquetada en una imagen Docker con Gunicorn.

## Construir y desplegar

```sh
docker build -t actividad7:1 .
docker run -d --name actividad7 -p 127.0.0.1:8080:8080 actividad7:1
curl http://127.0.0.1:8080/
curl http://127.0.0.1:8080/health
```

La ruta `/` responde `API funcionando con Docker`. La ruta `/health` devuelve `{"status":"ok"}`.

## Pipeline

El workflow `.github/workflows/docker.yml` construye la imagen, ejecuta un contenedor temporal, comprueba sus rutas HTTP y muestra sus logs. Se activa con cada push a `actividad-7-docker`.

Esta verificación usa un contenedor temporal en GitHub Actions. La configuración del workflow por sí sola no acredita que su ejecución haya terminado correctamente.
