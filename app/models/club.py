from app.database import get_db

class Club:
    @staticmethod
    def get_all():
        """Get all clubs"""
        db = get_db()
        clubs = db.execute('SELECT id, name, description, executive_id FROM clubs').fetchall()
        return [dict(club) for club in clubs]
    
    @staticmethod
    def get_by_id(club_id):
        """Get club by id"""
        db = get_db()
        club = db.execute('SELECT * FROM clubs WHERE id = ?', (club_id,)).fetchone()
        return dict(club) if club else None
    
    @staticmethod
    def create(name, description, executive_id=None):
        """Create a new club"""
        db = get_db()
        cursor = db.execute(
            'INSERT INTO clubs (name, description, executive_id) VALUES (?, ?, ?)',
            (name, description, executive_id)
        )
        db.commit()
        return cursor.lastrowid
