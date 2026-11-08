# Ficha de la aplicación APP-03

Programa que muestra, en diez opciones, la ficha técnica de una aplicación móvil antes de
publicarla: identificación, tamaño del APK, ingresos, versionCode, permisos, color del icono y
varias comprobaciones sobre tipos y redondeo.

**Módulo:** IC44 — Fundamentos de programación en Python
**Unidad:** 1 — Estructura de un programa y elementos del lenguaje
**Pareja:** 3
**Autores:** ARMO575 · alejandromoreno

## Aplicación descrita

| Dato | Valor |
|---|---|
| Código | APP-03 |
| Nombre | Horario de Bus |
| Paquete | es.transporte.horariobus |
| Versión | 2.1.0 |
| Tamaño del APK | 25_165_824 B (25.17 MB / 24.00 MiB) |
| Descargas y precio | 41_000 · 0.99 € |

## Ejecución desde Docker Hub

No hace falta descargar el repositorio ni tener Python instalado. Solo Docker.

```bash
docker run --rm --pull always arecmon605/ficha-app-03:1.0.0
```

Página de la imagen: https://hub.docker.com/r/arecmon605/ficha-app-03

## Ejecución en local

Requiere Python 3.10 o superior.

```bash
python3 -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
python ficha_app.py
```

## Construir la imagen

```bash
docker build -t ficha-app-03 .
docker run --rm ficha-app-03
```

## Integración continua

El repositorio cuenta con una pipeline de CI/CD en GitHub Actions (`.github/workflows/ci.yml`) ejecutada en un agente `ubuntu-latest` con dos etapas:
- **Comprobar**: se lanza en cada `push` a `main` y al subir etiquetas `v*`. Instala Python 3.14, verifica que el programa compila con `py_compile`, comprueba el cumplimiento de PEP 8 con `pycodestyle` y ejecuta las diez opciones.
- **Publicar**: se ejecuta únicamente cuando se sube una etiqueta de versión (`v*`) y la etapa anterior ha terminado sin errores. Inicia sesión en Docker Hub mediante el secreto `DOCKERHUB_TOKEN`, construye la imagen multiarquitectura (`linux/amd64` y `linux/arm64`) con Docker Buildx y la publica con la etiqueta de la versión (`1.0.0`) y `latest`.

## Estructura del proyecto

```
.
├── .github/workflows/ci.yml
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
└── ficha_app.py
```
