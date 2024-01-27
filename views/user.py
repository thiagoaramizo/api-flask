from flask import request, jsonify
from flask_login import login_required, current_user
import uuid
import bcrypt

from views.app import app # importação do app
from database import db
from models.user import User

@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    password = data["password"]
    hashed_password = bcrypt.hashpw( str.encode(password), bcrypt.gensalt() )

    if username and email and password:
        new_id = str(uuid.uuid4())
        new_user = User(username=username, email=email, password=hashed_password, id=new_id, role="user")
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
        if user.id == current_user.id or user.role == "admin":
            hashed_password = bcrypt.hashpw( str.encode(data["password"]), bcrypt.gensalt() )
            user.password = hashed_password
            db.session.commit()
            return jsonify({"message": "Usuário atualizado."})
        return jsonify({"message": "Operação não permitida."}), 403
    return jsonify({"message": "Usuário não encontrado."}), 404


@app.route("/user/<string:user_id>", methods=["DELETE"])
@login_required
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        if current_user.role != "admin" or current_user.id == user.id:
            return jsonify({"message": "Operação não permitida."}), 403
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "Usuário deletado."})
    
    return jsonify({"message": "Usuário não encontrado."}), 404
