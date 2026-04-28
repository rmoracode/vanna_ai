import os
import vanna
# Usamos una importación más segura
from vanna.remote import VannaDefault
from vanna.flask import VannaFlaskApp

# Configuración desde variables de entorno de Railway
VANNA_MODEL = os.getenv('VANNA_MODEL')
VANNA_API_KEY = os.getenv('VANNA_API_KEY')

# Inicializar Vanna
vn = VannaDefault(model=VANNA_MODEL, api_key=VANNA_API_KEY)

# Conexión a tu base de datos de Hostinger
vn.connect_to_postgres(
    host='72.61.2.146', 
    dbname='ventas_aje', 
    user='postgres', 
    password=os.getenv('PG_PASSWORD'), 
    port=5432
)

# Crear la aplicación Flask oficial de Vanna
app = VannaFlaskApp(vn)

if __name__ == '__main__':
    # Railway asigna el puerto automáticamente en la variable PORT
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
