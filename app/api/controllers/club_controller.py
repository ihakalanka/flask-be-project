from app.api.services.club_service import (
    get_clubs_service, get_club_service, create_club_service, get_club_members_service, assign_executive_service
)

def get_clubs():
    clubs = get_clubs_service()
    return clubs, 200

def get_club(club_id):
    club = get_club_service(club_id)
    if not club:
        return {'message': 'Club not found'}, 404
    return club, 200

def create_club(name, description, executive_id):
    club_id = create_club_service(name, description, executive_id)
    return {'message': 'Club created', 'club_id': club_id}, 201

def get_club_members(club_id):
    members = get_club_members_service(club_id)
    return members, 200

def assign_executive(club_id, executive_id):
    assign_executive_service(club_id, executive_id)
    return {'message': 'Executive assigned'}, 200