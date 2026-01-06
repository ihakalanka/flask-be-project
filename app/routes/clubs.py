from flask import Blueprint, request, jsonify
from app.api.controllers.club_controller import (
    get_clubs, get_club, create_club, get_club_members, assign_executive
)

clubs_bp = Blueprint('clubs', __name__)

@clubs_bp.route('/', methods=['GET'])
def get_clubs_route():
    result, status = get_clubs()
    return jsonify(result), status

@clubs_bp.route('/<int:club_id>', methods=['GET'])
def get_club_route(club_id):
    result, status = get_club(club_id)
    return jsonify(result), status

@clubs_bp.route('/', methods=['POST'])
def create_club_route():
    data = request.get_json()
    result, status = create_club(data['name'], data['description'], data.get('executive_id'))
    return jsonify(result), status

@clubs_bp.route('/<int:club_id>/members', methods=['GET'])
def get_club_members_route(club_id):
    result, status = get_club_members(club_id)
    return jsonify(result), status

@clubs_bp.route('/<int:club_id>/executive', methods=['PUT'])
def assign_executive_route(club_id):
    data = request.get_json()
    result, status = assign_executive(club_id, data['executive_id'])
    return jsonify(result), status