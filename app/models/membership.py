import sqlite3
from app.database import get_db

class Membership:
    @staticmethod
    def get_by_user(user_id):
        """Get memberships by user"""
        db = get_db()
        memberships = db.execute('''
            SELECT m.*, c.name as club_name, c.description as club_description
            FROM memberships m
            JOIN clubs c ON m.club_id = c.id
            WHERE m.user_id = ?
        ''', (user_id,)).fetchall()
        return [dict(membership) for membership in memberships]
    
    @staticmethod
    def get_by_club(club_id):
        """Get memberships by club"""
        db = get_db()
        memberships = db.execute('''
            SELECT m.*, u.username, u.email, u.role
            FROM memberships m
            JOIN users u ON m.user_id = u.id
            WHERE m.club_id = ?
        ''', (club_id,)).fetchall()
        return [dict(membership) for membership in memberships]
    
    @staticmethod
    def join_club(user_id, club_id):
        """Join a club"""
        db = get_db()
        try:
            cursor = db.execute(
                'INSERT INTO memberships (user_id, club_id) VALUES (?, ?)',
                (user_id, club_id)
            )
            db.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            return None  # Already a member
    
    @staticmethod
    def leave_club(user_id, club_id):
        """Leave a club"""
        db = get_db()
        db.execute('DELETE FROM memberships WHERE user_id = ? AND club_id = ?', (user_id, club_id))
        db.commit()