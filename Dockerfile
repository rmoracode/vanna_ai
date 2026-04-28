FROM python:3.11-slim
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir "vanna[openai]" pandas sqlalchemy psycopg2-binary flask flask-cors
EXPOSE 8080
CMD ["python", "main.py"]
