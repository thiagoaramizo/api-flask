from flask import request, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from controllers.app import app # importação do app
from database import db
from models.user import User


login_manager = LoginManager() # configurando o login
login_manager.init_app(app)
login_manager.login_view = 'login' # view de login

@login_manager.user_loader #definindo a função para recuperar o usuário logado
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    if username and password:
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return jsonify( {"message": "Autenticação realizada com sucesso", "id": user.id} )
    
    return jsonify({"message": "Credenciais invalidas"}), 400  


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso"})
