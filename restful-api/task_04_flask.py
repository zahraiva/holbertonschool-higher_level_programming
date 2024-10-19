#!/usr/bin/python3
from flask import Flask, request, jsonify

app = Flask(__name__)

all_users = {}


@app.route('/')
def home():
    return 'Welcome to the Flask API!'


@app.route('/data')
def data():
    return jsonify(list(all_users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def user(username):
    if username in all_users:
        return jsonify(all_users[username])
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    if data['username'] in all_users:
        return jsonify({"error": "Username already exists"}), 400

    all_users[data['username']] = {
        "username": data['username'],
        "name": data.get('name', ''),
        "age": data.get('age', None),
        "city": data.get('city', '')
    }
    return jsonify({"message": "User added", "user": all_users[data['username']]}), 201


if __name__ == "__main__":
    app.run(debug=True)
