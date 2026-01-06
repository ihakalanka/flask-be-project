from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from app.database import get_db

def register_user_service(username, email, password, role='General Member'):
    db = get_db()
    existing = db.execute('SELECT id FROM users WHERE username = ? OR email = ?', (username, email)).fetchone()
    if existing:
        return {'message': 'Username or email already exists'}, 400
    db.execute('INSERT INTO users (username, email, password_hash, role) VALUES (?, ?, ?, ?)',
               (username, email, generate_password_hash(password), role))
    db.commit()
    return {'message': 'User registered'}, 201

def login_user_service(username, password):
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    if user and check_password_hash(user['password_hash'], password):
        # Create JWT tokens
        access_token = create_access_token(
            identity=user['id'],
            additional_claims={'role': user['role'], 'username': user['username']}
        )
        refresh_token = create_refresh_token(identity=user['id'])
        
        return {
            'user_id': user['id'],
            'role': user['role'],
            'username': user['username'],
            'access_token': access_token,
            'refresh_token': refresh_token,
            'message': 'Logged in'
        }, 200
    return {'message': 'Invalid credentials'}, 401

def logout_user_service():
    return {'message': 'Logged out'}, 200
