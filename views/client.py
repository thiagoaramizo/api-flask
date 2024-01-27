from flask import request, jsonify
from flask_login import login_required, current_user
import uuid

from views.app import app # importação do app
from database import db
from models.client import Client

@app.route("/client", methods=['POST'])
@login_required
def create_client():
    data = request.get_json()
    new_client_id = str(uuid.uuid4())
    new_client = Client(id=new_client_id, name=data.get("name"), email=data.get("email", ""), cel=data.get("cel", ""), user_id=current_user.id)
    db.session.add(new_client)
    db.session.commit()
    return jsonify({"message": "Novo cliente criado com sucesso", "id": new_client_id }), 201


@app.route("/client", methods=['GET'])
@login_required
def list_client():
    clients = Client.query.filter_by(user_id=current_user.id)
    dict_clients = []
    for client in clients:
        dict_clients.append({
            "id": client.id,
            "name": client.name,
            "email": client.email,
            "cel": client.cel
        })
    return jsonify(dict_clients), 200


@app.route("/client/<string:id>", methods=['GET'])
@login_required
def get_client(id):
    client = Client.query.get(id)
    if client:
        return {"name": client.name, "email": client.email, "cel": client.cel, 'id': client.id}
    return jsonify({"message": "Cliente não encontrado."}), 404

#TODO
@app.route("/client/<string:id>", methods=['PUT'])
@login_required
def update_client(id):
    return jsonify({"message": "Endpoint ainda não implementado"}), 500

#TODO
@app.route("/client/<string:id>", methods=['DELETE'])
@login_required
def delete_client(id):
    return jsonify({"message": "Endpoint ainda não implementado"}), 500