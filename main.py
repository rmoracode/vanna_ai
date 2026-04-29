import os
from vanna.remote import VannaDefault
from vanna.flask import VannaFlaskApp

# Forzamos la lectura de variables
api_key = os.getenv('VANNA_API_KEY')
vanna_model = os.getenv('VANNA_MODEL')

try:
    # Inicialización
    vn = VannaDefault(model=vanna_model, api_key=api_key)

    # Conexión a Postgres (Asegúrate de que estos datos sean correctos)
    vn.connect_to_postgres(
        host='72.61.2.146', 
        dbname='ventas_aje', 
        user='postgres', 
        password=os.getenv('PG_PASSWORD'), 
        port=5432
    )

    app = VannaFlaskApp(vn)

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)))

except Exception as e:
    print(f"ERROR DE CONFIGURACIÓN: {str(e)}")
