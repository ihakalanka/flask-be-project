from app.models.event import Event

def get_events_service():
    return Event.get_all()

def get_event_service(event_id):
    return Event.get_by_id(event_id)

def get_club_events_service(club_id):
    return Event.get_by_club(club_id)

def create_event_service(club_id, title, description, event_date):
    return Event.create(club_id, title, description, event_date)

def update_event_service(event_id, title, description, event_date):
    Event.update(event_id, title, description, event_date)

def delete_event_service(event_id):
    Event.delete(event_id)