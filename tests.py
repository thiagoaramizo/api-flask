import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"
clients = []

def test_create_client():
    new_client_data = {
        "name": "Cliente de teste",
        "email": "email@email.com",
        "cel": "349999999"
    }
    response = requests.post(f"{BASE_URL}/clients", json=new_client_data)
    assert response.status_code == 201
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    clients.append(response_json['id'])

def test_get_clients():
    response = requests.get(f"{BASE_URL}/clients")
    assert response.status_code == 200
    response_json = response.json()
    assert "clients" in response_json
    assert "total_clients" in response_json

def test_get_client(): 
    if clients:
        client_id = clients[0]
        response = requests.get(f"{BASE_URL}/clients/{client_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['id'] == client_id
        assert "name" in response_json
        assert "email" in response_json
        assert "cel" in response_json

def test_update_client(): 
    payload = {
        "name": "Cliente de teste editado",
        "email": "email@email.com",
        "cel": "349999999"
    }
    if clients:
        client_id = clients[0]
        response = requests.put(f"{BASE_URL}/clients/{client_id}", json=payload)
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        response = requests.get(f"{BASE_URL}/clients/{client_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['name'] == payload["name"]
        assert response_json['email'] == payload["email"]
        assert response_json['cel'] == payload["cel"]

def test_delete_client(): 
    if clients:
        client_id = clients[0]
        response = requests.delete(f"{BASE_URL}/clients/{client_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        response = requests.get(f"{BASE_URL}/clients/{client_id}")
        assert response.status_code == 404