from flask import Flask, request, jsonify
import uuid
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from database import db
from models.user import User
from models.client import Client

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key" #configurando a Secret Key para validação de sessão
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db" #definindo a URI para o banco de dados

db.init_app(app) # vinculando o database com o app: executar o "flask shell -> db.create_all() -> db.session.commit()"

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


@app.route("/")
def api_status():
    return {
        "status": "API is running!"
    }


@app.route("/client", methods=['POST'])
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


# Executando o servidor
if __name__ == "__main__":
    app.run(debug=True)