from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_db_connection
from models import (
    get_all_animais, get_animal_by_id, create_animal, update_animal, delete_animal,
    get_all_cuidados, get_cuidado_by_id, create_cuidado, update_cuidado, delete_cuidado
)

app = Flask(__name__)
CORS(app, origins="http://localhost:3000")  # Permite requisições do frontend React

# -----------------------------
# ROTA DE BOAS-VINDAS
# -----------------------------

@app.route('/')
def home():
    return jsonify({
        "mensagem": "🎉 API do Zoológico está no ar!",
        "endpoints": {
            "/animais": "GET, POST, PUT (com ID), DELETE (com ID)",
            "/cuidados": "GET, POST, PUT (com ID), DELETE (com ID)"
        }
    }), 200

# -----------------------------
# ROTAS PARA ANIMAIS
# -----------------------------

@app.route('/animais', methods=['GET'])
def listar_animais():
    conn = get_db_connection()
    animais = get_all_animais(conn)
    conn.close()
    return jsonify(animais)

@app.route('/animais/<int:id>', methods=['GET'])
def obter_animal(id):
    conn = get_db_connection()
    animal = get_animal_by_id(conn, id)
    conn.close()
    if animal:
        return jsonify(animal)
    else:
        return jsonify({'erro': 'Animal não encontrado'}), 404

@app.route('/animais', methods=['POST'])
def adicionar_animal():
    data = request.get_json()
    conn = get_db_connection()
    animal_id = create_animal(conn, data)
    conn.close()
    return jsonify({'id': animal_id}), 201

@app.route('/animais/<int:id>', methods=['PUT'])
def atualizar_animal(id):
    data = request.get_json()
    conn = get_db_connection()
    update_animal(conn, id, data)
    conn.close()
    return jsonify({'mensagem': 'Animal atualizado com sucesso'})

@app.route('/animais/<int:id>', methods=['DELETE'])
def remover_animal(id):
    conn = get_db_connection()
    delete_animal(conn, id)
    conn.close()
    return jsonify({'mensagem': 'Animal removido com sucesso'})

# -----------------------------
# ROTAS PARA CUIDADOS
# -----------------------------

@app.route('/cuidados', methods=['GET'])
def listar_cuidados():
    conn = get_db_connection()
    cuidados = get_all_cuidados(conn)
    conn.close()
    return jsonify(cuidados)

@app.route('/cuidados/<int:id>', methods=['GET'])
def obter_cuidado(id):
    conn = get_db_connection()
    cuidado = get_cuidado_by_id(conn, id)
    conn.close()
    if cuidado:
        return jsonify(cuidado)
    else:
        return jsonify({'erro': 'Cuidado não encontrado'}), 404

@app.route('/cuidados', methods=['POST'])
def adicionar_cuidado():
    data = request.get_json()
    conn = get_db_connection()
    cuidado_id = create_cuidado(conn, data)
    conn.close()
    return jsonify({'id': cuidado_id}), 201

@app.route('/cuidados/<int:id>', methods=['PUT'])
def atualizar_cuidado(id):
    data = request.get_json()
    conn = get_db_connection()
    update_cuidado(conn, id, data)
    conn.close()
    return jsonify({'mensagem': 'Cuidado atualizado com sucesso'})

@app.route('/cuidados/<int:id>', methods=['DELETE'])
def remover_cuidado(id):
    conn = get_db_connection()
    delete_cuidado(conn, id)
    conn.close()
    return jsonify({'mensagem': 'Cuidado removido com sucesso'})
