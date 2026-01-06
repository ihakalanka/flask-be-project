from app.database import get_db
from app.models.club import Club
from app.models.membership import Membership

def get_clubs_service():
    return Club.get_all()

def get_club_service(club_id):
    return Club.get_by_id(club_id)

def create_club_service(name, description, executive_id):
    # Check if executive is valid, etc.
    return Club.create(name, description)

def get_club_members_service(club_id):
    return Membership.get_by_club(club_id)

def assign_executive_service(club_id, executive_id):
    # Update club executive
    db = get_db()
    db.execute('UPDATE clubs SET executive_id = ? WHERE id = ?', (executive_id, club_id))
    db.commit()