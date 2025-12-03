#!/usr/bin/python3
"""Flask API with multiple endpoints and in-memory user storage."""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = {}


@app.route("/", methods=["GET"])
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """Status endpoint."""
    return "OK"


@app.route("/data", methods=["GET"])
def get_usernames():
    """Return list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return full user object by username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user via POST request."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    user_data = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    # Listen on all interfaces so container/test runner can connect
    app.run(host="0.0.0.0", port=5000)

