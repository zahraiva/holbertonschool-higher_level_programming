#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    if not users:
        return jsonify({"message": "No users found"}), 200
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if 'username' not in data or 'name' not in data or 'age' not in data or 'city' not in data:
        return jsonify({"error": "All fields (username, name, age, city) are required"}), 400
    if data['username'] in users:
        return jsonify({"error": "Username already exists"}), 400
    users[data['username']] = {
        "username": data['username'],
        "name": data['name'],
        "age": data['age'],
        "city": data['city']
    }
    return jsonify({"message": "User added", "user": users[data['username']]})

if __name__ == "__main__":
    app.run(debug=True)
