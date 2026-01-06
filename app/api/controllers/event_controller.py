from app.api.services.event_service import (
    get_events_service, get_event_service, get_club_events_service,
    create_event_service, update_event_service, delete_event_service
)

def get_events():
    events = get_events_service()
    return events, 200

def get_event(event_id):
    event = get_event_service(event_id)
    if not event:
        return {'message': 'Event not found'}, 404
    return event, 200

def get_club_events(club_id):
    events = get_club_events_service(club_id)
    return events, 200

def create_event(club_id, title, description, event_date):
    event_id = create_event_service(club_id, title, description, event_date)
    return {'message': 'Event created', 'event_id': event_id}, 201

def update_event(event_id, title, description, event_date):
    update_event_service(event_id, title, description, event_date)
    return {'message': 'Event updated'}, 200

def delete_event(event_id):
    delete_event_service(event_id)
    return {'message': 'Event deleted'}, 200