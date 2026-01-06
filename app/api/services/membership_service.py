from app.models.membership import Membership

def get_user_memberships_service(user_id):
    return Membership.get_by_user(user_id)

def join_club_service(user_id, club_id):
    return Membership.join_club(user_id, club_id)

def leave_club_service(user_id, club_id):
    Membership.leave_club(user_id, club_id)