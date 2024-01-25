from flask import request, jsonify
from flask_login import login_required, current_user
import uuid

from controllers.app import app # importação do app
from database import db
from models.client import Client

@app.route("/client", methods=['POST'])
@login_required
def create_client():
    data = request.get_json()
    new_client_id = str(uuid.uuid4())
    new_client = Client(id=new_client_id, name=data.get("name"), email=data.get("email", ""), cel=data.get("cel", ""), user=current_user.id)
    db.session.add(new_client)
    db.session.commit()
    return jsonify({"message": "Novo cliente criado com sucesso", "id": new_client_id }), 201


@app.route("/client/<string:id>", methods=['GET'])
def get_client(id):
    client = Client.query.get(id)
    if client:
        return {"name": client.name, "email": client.email, "cel": client.cel, 'id': client.id}
    return jsonify({"message": "Cliente não encontrado."}), 404
