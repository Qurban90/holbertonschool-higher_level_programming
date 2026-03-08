#!/usr/bin/env python3
"""
Flask API exercise
"""
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

# Users stored in-memory
users = {}


@app.route("/")
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    """Return list of all usernames"""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return status OK"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return user data by username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    return make_response(jsonify({"error": "User not found"}), 404)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user via POST request"""
    try:
        data = request.get_json()
    except Exception:
        return make_response(jsonify({"error": "Invalid JSON"}), 400)

    if not data:
        return make_response(jsonify({"error": "Invalid JSON"}), 400)

    username = data.get("username")
    if not username:
        return make_response(jsonify({"error": "Username is required"}), 400)

    if username in users:
        return make_response(jsonify({"error": "Username already exists"}), 409)

    # Save the user
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }

    return make_response(
        jsonify({"message": "User added", "user": users[username]}), 201
    )


if __name__ == "__main__":
    # Run on all interfaces so it works in Docker too
    app.run(host="0.0.0.0", port=5000)
