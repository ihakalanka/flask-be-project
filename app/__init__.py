from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.database import init_db, db_exists
from datetime import timedelta
import os

def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = 'uniclubs.db'
    
    # Flask Secret Key for sessions
    app.config['SECRET_KEY'] = '10f1da6f2ceadd0bb2f77adc87c13efb6a0a221122c86335dc4f43edabf0250f'
    
    # JWT Configuration
    app.config['JWT_SECRET_KEY'] = 'b121b852efc3d9077b5d9def1fb7a89d1468600e793dc49893bcafd435a0f089'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)
    
    # JWT Cookie Configuration (HTTP-only cookies for security)
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_COOKIE_SECURE'] = False  # Set to True in production with HTTPS
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False  # Disable CSRF for development
    app.config['JWT_COOKIE_SAMESITE'] = 'Lax'  # Prevents CSRF attacks
    app.config['JWT_ACCESS_COOKIE_NAME'] = 'access_token'
    app.config['JWT_REFRESH_COOKIE_NAME'] = 'refresh_token'
    app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
    app.config['JWT_REFRESH_COOKIE_PATH'] = '/'
    
    # Initialize JWT
    jwt = JWTManager(app)
    
    # Enable CORS with explicit configuration
    CORS(app, 
         resources={r"/*": {"origins": "http://localhost:3000"}},
         supports_credentials=True,
         allow_headers=["Content-Type", "Authorization"],
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    )
    
    # Initialize database (recreate on each cold start for Vercel)
    with app.app_context():
        # On Vercel, always init since /tmp is ephemeral
        if os.environ.get('VERCEL') or not db_exists():
            init_db()
            from app.mock_data import insert_mock_data
            insert_mock_data()
    
    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.clubs import clubs_bp
    from app.routes.events import events_bp
    from app.routes.memberships import memberships_bp
    from app.routes.dashboard import dashboard_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(clubs_bp, url_prefix='/clubs')
    app.register_blueprint(events_bp, url_prefix='/events')
    app.register_blueprint(memberships_bp, url_prefix='/memberships')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    
    # Health check endpoint
    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({
            'status': 'healthy',
            'service': 'UniClub Manager API',
            'version': '1.0.0'
        }), 200
    
    # Root endpoint
    @app.route('/', methods=['GET'])
    def root():
        return jsonify({
            'message': 'UniClub Manager API',
            'health': '/health',
            'docs': '/api/docs'
        }), 200
    
    return app
