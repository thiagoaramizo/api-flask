from database import db #importando a instância do banco de dados
from controllers.app import app #importanto a instância do app
import controllers.user #controlador do usuário
import controllers.auth #controlador de autenticação
import controllers.client #controlador do cliente


#app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key" #configurando a Secret Key para validação de sessão
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db" #definindo a URI para o banco de dados

db.init_app(app) # vinculando o database com o app: executar o "flask shell -> db.create_all() -> db.session.commit()"

@app.route("/")
def api_status():
    return {
        "message": "API is running!"
    }

# Executando o servidor
if __name__ == "__main__":
    app.run(debug=True)