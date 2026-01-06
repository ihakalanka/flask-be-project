from flask import Blueprint, request, jsonify
from app.api.controllers.membership_controller import (
    get_user_memberships, join_club, leave_club
)

memberships_bp = Blueprint('memberships', __name__)

@memberships_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_memberships_route(user_id):
    result, status = get_user_memberships(user_id)
    return jsonify(result), status

@memberships_bp.route('/', methods=['POST'])
def join_club_route():
    data = request.get_json()
    result, status = join_club(data['user_id'], data['club_id'])
    return jsonify(result), status

@memberships_bp.route('/', methods=['DELETE'])
def leave_club_route():
    data = request.get_json()
    result, status = leave_club(data['user_id'], data['club_id'])
    return jsonify(result), status