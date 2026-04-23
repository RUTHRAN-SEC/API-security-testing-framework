from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)
SECRET = "secret123"

users = {
    1: {"name": "Alice", "role": "user"},
    2: {"name": "Bob", "role": "admin"}
}

@app.route("/login", methods=["POST"])
def login():
    user_id = request.json.get("user_id")
    token = jwt.encode({"user_id": user_id}, SECRET, algorithm="HS256")
    return jsonify({"token": token})

# Vulnerable API (BOLA)
@app.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return jsonify(users.get(user_id, {}))

# No Rate Limit
@app.route("/data", methods=["GET"])
def data():
    return jsonify({"data": "sensitive info"})

# API Key Exposure
@app.route("/config", methods=["GET"])
def config():
    return jsonify({"api_key": "12345-SECRET-KEY"})

if __name__ == "__main__":
    app.run(debug=True)
