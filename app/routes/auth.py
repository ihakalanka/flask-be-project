from flask import Blueprint, request, session, jsonify
from flask_jwt_extended import set_access_cookies, set_refresh_cookies, unset_jwt_cookies, jwt_required, get_jwt_identity
from app.api.controllers.auth_controller import register_user, login_user, logout_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    result, status = register_user(data['username'], data['email'], data['password'], data.get('role', 'General Member'))
    return jsonify(result), status

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result, status = login_user(data['username'], data['password'])
    
    if status == 200:
        session['user_id'] = result['user_id']
        session['role'] = result['role']
        
        # Create response with user data (no tokens in body)
        response = jsonify({
            'user_id': result['user_id'],
            'role': result['role'],
            'username': result['username'],
            'message': result['message']
        })
        
        # Set HTTP-only cookies for tokens
        set_access_cookies(response, result['access_token'])
        set_refresh_cookies(response, result['refresh_token'])
        
        return response, status
    else:
        return jsonify(result), status

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    # Get the identity from the refresh token
    current_user_id = get_jwt_identity()
    
    # Get user details from database
    from app.database import get_db
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE id = ?', (current_user_id,)).fetchone()
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    # Create new access token
    from flask_jwt_extended import create_access_token
    new_access_token = create_access_token(
        identity=user['id'],
        additional_claims={'role': user['role'], 'username': user['username']}
    )
    
    # Set new access token cookie
    response = jsonify({'message': 'Token refreshed successfully'})
    set_access_cookies(response, new_access_token)
    
    return response, 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    result, status = logout_user()
    session.clear()
    
    # Clear JWT cookies
    response = jsonify(result)
    unset_jwt_cookies(response)
    
    return response, status
