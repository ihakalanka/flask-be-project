from app.database import get_db

class Event:
    @staticmethod
    def get_all():
        """Get all events"""
        db = get_db()
        events = db.execute('SELECT * FROM events ORDER BY event_date ASC').fetchall()
        return [dict(event) for event in events]
    
    @staticmethod
    def get_by_id(event_id):
        """Get event by id"""
        db = get_db()
        event = db.execute('SELECT * FROM events WHERE id = ?', (event_id,)).fetchone()
        return dict(event) if event else None
    
    @staticmethod
    def get_by_club(club_id):
        """Get events by club"""
        db = get_db()
        events = db.execute('SELECT * FROM events WHERE club_id = ? ORDER BY event_date ASC', (club_id,)).fetchall()
        return [dict(event) for event in events]
    
    @staticmethod
    def create(club_id, title, description, event_date):
        """Create a new event"""
        db = get_db()
        cursor = db.execute(
            'INSERT INTO events (club_id, title, description, event_date) VALUES (?, ?, ?, ?)',
            (club_id, title, description, event_date)
        )
        db.commit()
        return cursor.lastrowid
    
    @staticmethod
    def update(event_id, title, description, event_date):
        """Update an event"""
        db = get_db()
        db.execute(
            'UPDATE events SET title = ?, description = ?, event_date = ? WHERE id = ?',
            (title, description, event_date, event_id)
        )
        db.commit()
    
    @staticmethod
    def delete(event_id):
        """Delete an event"""
        db = get_db()
        db.execute('DELETE FROM events WHERE id = ?', (event_id,))
        db.commit()