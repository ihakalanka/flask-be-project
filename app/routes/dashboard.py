from flask import Blueprint, request, jsonify
from app.api.controllers.membership_controller import get_user_memberships
from app.api.controllers.event_controller import get_events

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/<int:user_id>', methods=['GET'])
def get_dashboard(user_id):
    # Get user's clubs
    memberships, _ = get_user_memberships(user_id)
    clubs = [m['club_name'] for m in memberships]
    
    # Get upcoming events from user's clubs
    club_ids = [m['club_id'] for m in memberships]
    if club_ids:
        # For simplicity, get all events and filter
        all_events, _ = get_events()
        user_events = [e for e in all_events if e['club_id'] in club_ids]
    else:
        user_events = []
    
    return jsonify({
        'clubs': clubs,
        'upcoming_events': user_events
    }), 200