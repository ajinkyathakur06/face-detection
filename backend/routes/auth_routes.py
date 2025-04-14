from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Extract data from the request
    name = data.get('name')
    username = data.get('username')
    password = data.get('password')

    # Validate the input
    if not name or not username or not password:
        return jsonify({'message': 'Missing fields'}), 400

    # Check if user already exists
    if User.get_user_by_username(username):
        return jsonify({'message': 'User already exists'}), 409

    # Hash the password before saving
    hashed_password = generate_password_hash(password)

    # Create a new user record in the database
    new_user = User(name=name, username=username, password=hashed_password)
    new_user.save()

    return jsonify({'message': 'User registered successfully'}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.get_user_by_username(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"message": "Invalid credentials!"}), 401

    return jsonify({"message": "Login successful!"}), 200
