#!/usr/bin/python3
from flask import Flask, request, jsonify

app = Flask(__name__)

users_data = {}


@app.route('/')
def welcome_message():
    return 'Welcome to the Flask API!'


@app.route('/data')
def list_users():
    return jsonify(list(users_data.keys()))


@app.route('/add_user', methods=['POST'])
def create_user():
    user_info = request.json
    if user_info is None or 'username' not in user_info:
        return jsonify({'error': 'Username is required'}), 400
    
    user_info['username'] = user_info.get('username')
    users_data[user_info['username']] = {
        'username': user_info['username'],
        'name': user_info.get('name'),
        'age': user_info.get('age'),
        'city': user_info.get('city')
    }
    return jsonify({'message': 'User added successfully', 'user': users_data[user_info['username']]}), 201


@app.route('/users/<username>')
def retrieve_user(username):
    if username not in users_data:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users_data[username])


@app.route('/status')
def api_status():
    return "OK"


if __name__ == "__main__":
    app.run()
