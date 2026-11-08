FROM python:3.14-slim

LABEL org.opencontainers.image.title="Ficha técnica de la aplicación APP-03 (Horario de Bus)"
LABEL org.opencontainers.image.authors="ARMO575 · alejandromoreno"
LABEL org.opencontainers.image.source="https://github.com/ARMO575/ficha-app-03"

WORKDIR /app

COPY ficha_app.py .

CMD ["python", "ficha_app.py"]
