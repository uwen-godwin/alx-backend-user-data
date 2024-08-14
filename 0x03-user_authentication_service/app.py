#!/usr/bin/env python3
"""
Flask app for user authentication
"""

from flask import Flask, request, jsonify
from auth import Auth

app = Flask(__name__)
AUTH = Auth()

@app.route("/", methods=["GET"])
def index():
    """Basic welcome route"""
    return jsonify({"message": "Bienvenue"}), 200

@app.route("/users", methods=["POST"])
def users():
    """POST /users route to register a new user"""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
