import os
import vanna as vn
from vanna.openai import OpenAI_Chat
from vanna.vannadb import VannaDB_VectorStore
from flask import Flask, request, jsonify
from flask_cors import CORS

# 1. LEER VARIABLES (Deben llamarse igual en el panel de Railway)
# os.getenv busca el nombre exacto de la variable de entorno
vanna_key = os.getenv('VANNA_API_KEY')
vanna_model = os.getenv('VANNA_MODEL')
openai_key = os.getenv('OPENAI_API_KEY')
pg_pass = os.getenv('PG_PASSWORD')

# 2. CONFIGURACIÓN DE VANNA
class MyVanna(VannaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        VannaDB_VectorStore.__init__(self, vanna_model=vanna_model, vanna_api_key=vanna_key, config=config)
        OpenAI_Chat.__init__(self, config={'api_key': openai_key, 'model': 'gpt-4o-mini'})

vn = MyVanna()

# 3. CONEXIÓN A POSTGRES (Hostinger)
vn.connect_to_postgres(
    host='72.61.2.146', 
    dbname='ventas_aje', 
    user='postgres', 
    password=pg_pass, # Aquí usa la variable leída arriba
    port=5432
)

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    # Esto genera el SQL, lo ejecuta y devuelve la respuesta
    answer = vn.ask(question, print_results=False)
    return jsonify({"answer": str(answer)})

if __name__ == '__main__':
    # Railway asigna un puerto dinámico, os.getenv('PORT') lo detecta
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
