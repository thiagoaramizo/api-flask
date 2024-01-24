from flask import Flask

app = Flask(__name__)

@app.route("/")
def api_status():
    return {
        "status": "API is running!"
    }

@app.route("/clients")
def get_clients():
    return {
        "clients" : []
    }

if __name__ == "__main__":
    app.run(debug=True)