from flask import Blueprint, request, jsonify
from app.api.controllers.event_controller import (
    get_events, get_event, get_club_events, create_event, update_event, delete_event
)

events_bp = Blueprint('events', __name__)

@events_bp.route('/', methods=['GET'])
def get_events_route():
    result, status = get_events()
    return jsonify(result), status

@events_bp.route('/<int:event_id>', methods=['GET'])
def get_event_route(event_id):
    result, status = get_event(event_id)
    return jsonify(result), status

@events_bp.route('/club/<int:club_id>', methods=['GET'])
def get_club_events_route(club_id):
    result, status = get_club_events(club_id)
    return jsonify(result), status

@events_bp.route('/', methods=['POST'])
def create_event_route():
    data = request.get_json()
    result, status = create_event(data['club_id'], data['title'], data['description'], data['event_date'])
    return jsonify(result), status

@events_bp.route('/<int:event_id>', methods=['PUT'])
def update_event_route(event_id):
    data = request.get_json()
    result, status = update_event(event_id, data['title'], data['description'], data['event_date'])
    return jsonify(result), status

@events_bp.route('/<int:event_id>', methods=['DELETE'])
def delete_event_route(event_id):
    result, status = delete_event(event_id)
    return jsonify(result), status