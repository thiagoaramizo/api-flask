from flask import request, jsonify
from flask_login import login_required, current_user
import uuid

from views.app import app # importação do app
from database import db
from models.user import User
from models.form.form import Form
from models.form.label import Label

@app.route("/form", methods=['POST'])
@login_required
def create_form():
    data = request.get_json()
    new_form_id = str(uuid.uuid4())
    name = data.get("name")
    privacy = data.get("privacy")
    description = data.get("description")
    status = data.get("status", 1)
    labels = data.get("labels")
    if name and privacy and status:
        new_form = Form(id=new_form_id, 
                        name=name,
                        description=description,
                        privacy=privacy, 
                        status=status, 
                        user_id=current_user.id)
        db.session.add(new_form)
        db.session.commit()
        if labels:
            for label in labels: 
                label_id = str(uuid.uuid4())
                form_id = new_form_id
                label_name = label["name"]
                label_input = label["input"]
                label_order = label["order"]
                label_description =  label["description"]
                label_required =  label["required"]
                label_options = label["options"]
                label_status = label["status"]
                new_label = Label(id=label_id, 
                                  form_id=form_id, 
                                  name=label_name, 
                                  input=label_input, 
                                  order=label_order, 
                                  description=label_description, 
                                  required=label_required, 
                                  options=label_options, 
                                  status=label_status )
                db.session.add(new_label)
            db.session.commit()
        return jsonify({"message": "Novo formulário criado com sucesso", "id": new_form_id }), 201
    return jsonify({"message": "Erro ao criar o formulário"}), 400

@app.route("/form", methods=['GET'])
@login_required
def list_form():
    forms = Form.query.filter_by(user_id=current_user.id)
    dict_forms = []
    for form in forms:
        dict_forms .append({
            "id": form.id,
            "name": form.name,
            "description": form.description,
            "privacy": form.privacy,
        })
    return jsonify(dict_forms ), 200

#TODO
@app.route("/form/<string:id>", methods=['GET'])
@login_required
def get_form(id):
    return jsonify({"message": "Endpoint ainda não implementado"}), 500

#TODO
@app.route("/form/<string:id>", methods=['PUT'])
@login_required
def update_form(id):
    return jsonify({"message": "Endpoint ainda não implementado"}), 500

#TODO
@app.route("/form/<string:id>", methods=['DELETE'])
@login_required
def delete_form(id):
    return jsonify({"message": "Endpoint ainda não implementado"}), 500