import os
from vanna.remote import VannaDefault
from vanna.flask import VannaFlaskApp

# 1. Configuración simplificada
# VannaDefault usa el motor de Vanna para conectar todo más fácil
vn = VannaDefault(
    model=os.getenv('VANNA_MODEL'), 
    api_key=os.getenv('VANNA_API_KEY')
)

# 2. Conexión a tu base de datos de Hostinger
vn.connect_to_postgres(
    host='72.61.2.146', 
    dbname='ventas_aje', 
    user='postgres', 
    password=os.getenv('PG_PASSWORD'), 
    port=5432
)

# 3. Lanzar la App oficial
# Esto te dará una interfaz web Y una API para n8n automáticamente
app = VannaFlaskApp(vn)

if __name__ == '__main__':
    # Railway asigna el puerto automáticamente
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
