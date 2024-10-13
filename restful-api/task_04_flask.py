#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    print("Home route accessed")
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    print("Data route accessed")
    if not users:
        print("No users found")
        return jsonify({"message": "No users found"}), 200
    print(f"Users found: {list(users.keys())}")
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    print("Status route accessed")
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    print(f"Fetching user: {username}")
    user = users.get(username)
    if user:
        print(f"User found: {user}")
        return jsonify(user)
    print(f"User {username} not found")
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    print(f"Data received for adding user: {data}")
    if 'username' not in data or 'name' not in data or 'age' not in data or 'city' not in data:
        print("Missing required fields")
        return jsonify({"error": "All fields (username, name, age, city) are required"}), 400
    if data['username'] in users:
        print(f"Username {data['username']} already exists")
        return jsonify({"error": "Username already exists"}), 400
    users[data['username']] = {
        "username": data['username'],
        "name": data['name'],
        "age": data['age'],
        "city": data['city']
    }
    print(f"User {data['username']} added")
    return jsonify({"message": "User added", "user": users[data['username']]})

if __name__ == "__main__":
    if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, use_debugger=False)

