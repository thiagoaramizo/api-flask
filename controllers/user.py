from flask import request, jsonify
from flask_login import login_required, current_user
import uuid

from controllers.app import app # importação do app
from database import db
from models.user import User

@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    password = data["password"]
    if username and email and password:
        new_id = str(uuid.uuid4())
        new_user = User(username=username, email=email, password=password, id=new_id)
        db.session.add(new_user)
        db.session.commit()
        return jsonify( {"message": "Usuário criado com sucesso", "id": new_id} )
    return jsonify({"message": "Dados invalidos"}), 400


@app.route("/user/<string:user_id>", methods=["GET"])
@login_required
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return {"username": user.username, "email": user.email}
    return jsonify({"message": "Usuário não encontrado."}), 404


@app.route("/user/<string:user_id>", methods=["PUT"])
@login_required
def update_password(user_id):
    user = User.query.get(user_id)
    data = request.get_json()
    if user and data["password"]:
        user.password = data["password"]
        db.session.commit()
        return jsonify({"message": "Usuário atualizado."})
    return jsonify({"message": "Usuário não encontrado."}), 404


@app.route("/user/<string:user_id>", methods=["DELETE"])
@login_required
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:

        if current_user.id == user.id: #verificando se não é o mesmo usuário
            return jsonify({"message": "Remoção não permitida."}), 403
   
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "Usuário deletado."})
    
    return jsonify({"message": "Usuário não encontrado."}), 404
