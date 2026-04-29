import os
import vanna
from vanna.remote import VannaDefault
from vanna.flask import VannaFlaskApp

# Leemos las variables de Railway
vanna_model = os.getenv('VANNA_MODEL')
vanna_api_key = os.getenv('VANNA_API_KEY')

# Inicialización robusta
vn = VannaDefault(model=vanna_model, api_key=vanna_api_key)

# Intentamos conectar a Postgres. Si falla, el servidor seguirá vivo para que lo veas.
try:
    vn.connect_to_postgres(
        host='72.61.2.146', 
        dbname='ventas_aje', 
        user='postgres', 
        password=os.getenv('PG_PASSWORD'), 
        port=5432
    )
    print("Conexión a Postgres Exitosa")
except Exception as e:
    print(f"Error conectando a Postgres: {e}")

# Iniciamos la App
app = VannaFlaskApp(vn)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
