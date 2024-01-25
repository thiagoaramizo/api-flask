from flask import Flask, request, jsonify
from markupsafe import escape
import uuid
from models.client import Client

app = Flask(__name__)

clients = []

@app.route("/")
def api_status():
    return {
        "status": "API is running!"
    }


@app.route("/clients", methods=['POST'])
def create_client():
    data = request.get_json()
    new_client = Client(id=str(uuid.uuid4()), name=data.get("name"), email=data.get("email", ""), cel=data.get("cel", ""))
    clients.append(new_client)
    print( new_client.to_dict() )
    print(clients)
    return jsonify({"message": "Novo cliente criado com sucesso"}), 201


@app.route("/clients", methods=['GET'])
def get_clients():
    clients_list = [ client.to_dict() for client in clients ]
    output = {
        "clients": clients_list,
        "total_clients": len(clients_list)
    }
    return output


@app.route("/clients/<string:id>", methods=['GET'])
def get_client_by_id(id):
    print(id)
    for client in clients:
        if client.get_id() == id:
            return jsonify(client.to_dict())        
    return jsonify({"message": "Cliente não encontrado."}), 404


@app.route("/clients/<string:id>", methods=['PUT'])
def edit_client(id):
    client = None
    for c in clients:
        if c.get_id() == id:
            client = c
            break
    if client == None:
        return jsonify({"message": "Cliente não encontrado."}), 404
    
    data = request.get_json()
    client.set_name(data["name"])
    client.set_email(data["email"])
    client.set_cel(data["cel"])
    print( client )
    
    return jsonify({"message": "Cliente editado com sucesso."})


@app.route("/clients/<string:id>", methods=['DELETE'])
def delete_client(id):
    index_target = None
    for index, client in enumerate(clients):
        if client.get_id() == id:
            index_target = index
            break
    if index_target == None:
        return jsonify({"message": "Cliente não encontrado."}), 404
    del( clients[index_target] )
    return jsonify({"message": "Cliente deletado."})

if __name__ == "__main__":
    app.run(debug=True)