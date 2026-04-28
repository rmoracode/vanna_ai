import vanna as vn
from vanna.openai import OpenAI_Chat
from vanna.vannadb import VannaDB_VectorStore
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# 1. CLASE DE CONFIGURACIÓN
class MyVanna(VannaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        VannaDB_VectorStore.__init__(self, vanna_model='TU_MODEL_NAME', vanna_api_key='TU_VANNA_API_KEY', config=config)
        OpenAI_Chat.__init__(self, config={'api_key': 'TU_OPENAI_API_KEY', 'model': 'gpt-4o-mini'})

vn = MyVanna()

# 2. CONEXIÓN (La IP de tu Hostinger)
vn.connect_to_postgres(
    host='72.61.2.146', 
    dbname='ventas_aje', 
    user='postgres', 
    password='TU_PASSWORD_POSTGRES', 
    port=5432
)

# 3. SERVIDOR API PARA N8N
app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    # Vanna traduce lenguaje natural -> SQL -> Ejecuta -> Devuelve respuesta
    answer = vn.ask(question, print_results=False)
    return jsonify({"answer": str(answer)})

if __name__ == '__main__':
    # Railway usa la variable de entorno PORT
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
