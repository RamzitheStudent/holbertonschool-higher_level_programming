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
