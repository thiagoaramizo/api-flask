from database import db #importando a instância do banco de dados
from views.app import app #importanto a instância do app
import views.user #controlador do usuário
import views.auth #controlador de autenticação
import views.client #controlador do cliente
import views.form #controlador do cliente


#app importado
app.config['SECRET_KEY'] = "your_secret_key" #configurando a Secret Key para validação de sessão
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db" #definindo a URI para o banco de dados
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql:///root:pass@127.0.0.1:3306/flask-crud"

db.init_app(app) # vinculando o database com o app: executar o "flask shell -> db.create_all() -> db.session.commit()"

@app.route("/")
def api_status():
    return {
        "message": "API is running!"
    }

# Executando o servidor
if __name__ == "__main__":
    app.run(debug=True)