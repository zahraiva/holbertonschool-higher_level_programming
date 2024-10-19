#!/usr/bin/python3
from flask import Flask, request, jsonify

app = Flask(__name__)

user_data = {}


@app.route('/')
def home_page():
    return 'Welcome to the Flask API!'


@app.route('/data')
def retrieve_usernames():
    return jsonify(list(user_data.keys()))


@app.route('/status')
def check_status():
    return "OK"


@app.route('/users/<username>')
def fetch_user(username):
    if username in user_data:
        return jsonify(user_data[username])
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def register_user():
    new_user = request.get_json()
    if not new_user or 'username' not in new_user:
        return jsonify({"error": "Username is required"}), 400
    if new_user['username'] in user_data:
        return jsonify({"error": "Username already exists"}), 400

    user_data[new_user['username']] = {
        "username": new_user['username'],
        "name": new_user.get('name', ''),
        "age": new_user.get('age', None),
        "city": new_user.get('city', '')
    }
    return jsonify({"message": "User added", "user": user_data[new_user['username']]}), 201


if __name__ == "__main__":
    app.run(debug=True)
