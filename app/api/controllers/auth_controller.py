from app.api.services.auth_service import register_user_service, login_user_service, logout_user_service

def register_user(username, email, password, role='General Member'):
    return register_user_service(username, email, password, role)

def login_user(username, password):
    return login_user_service(username, password)

def logout_user():
    return logout_user_service()
