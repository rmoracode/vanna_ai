FROM python:3.11-slim

# Instalamos librerías del sistema necesarias para PostgreSQL y Python
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Instalación FORZADA de las librerías
RUN pip install --no-cache-dir \
    "vanna[openai]" \
    pandas \
    sqlalchemy \
    psycopg2-binary \
    flask \
    flask-cors

# Copiamos todo tu código al servidor
COPY . .

# Railway usa el puerto 8080 por defecto
EXPOSE 8080

# Comando para arrancar el cerebro
CMD ["python", "main.py"]
