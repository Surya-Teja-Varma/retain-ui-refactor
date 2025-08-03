from flask import Blueprint, request, jsonify
from models.user_model import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user,
    search_users_by_name,
    login_user
)

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify([dict(user) for user in users])

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(dict(user))
    return jsonify({"error": "User not found"}), 404

@user_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not all(k in data for k in ('name', 'email', 'password')):
        return jsonify({"error": "Missing required fields"}), 400
    create_user(data['name'], data['email'], data['password'])
    return jsonify({"message": "User created"}), 201

@user_bp.route('/user/<int:user_id>', methods=['PUT'])
def modify_user(user_id):
    data = request.get_json()
    if not all(k in data for k in ('name', 'email')):
        return jsonify({"error": "Missing required fields"}), 400
    update_user(user_id, data['name'], data['email'])
    return jsonify({"message": "User updated"})

@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    delete_user(user_id)
    return jsonify({"message": f"User {user_id} deleted"})

@user_bp.route('/search', methods=['GET'])
def search_users():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Please provide a name"}), 400
    users = search_users_by_name(name)
    return jsonify([dict(user) for user in users])

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not all(k in data for k in ('email', 'password')):
        return jsonify({"error": "Missing credentials"}), 400
    user = login_user(data['email'], data['password'])
    if user:
        return jsonify({"status": "success", "user_id": user["id"]})
    return jsonify({"status": "failed"}), 401
