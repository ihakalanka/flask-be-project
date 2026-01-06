from app.api.services.membership_service import (
    get_user_memberships_service, join_club_service, leave_club_service
)

def get_user_memberships(user_id):
    memberships = get_user_memberships_service(user_id)
    return memberships, 200

def join_club(user_id, club_id):
    membership_id = join_club_service(user_id, club_id)
    if membership_id:
        return {'message': 'Joined club', 'membership_id': membership_id}, 201
    else:
        return {'message': 'Already a member'}, 400

def leave_club(user_id, club_id):
    leave_club_service(user_id, club_id)
    return {'message': 'Left club'}, 200