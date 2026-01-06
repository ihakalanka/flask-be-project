import sqlite3
import os
from flask import g, current_app

def get_db_path():
    """Get the appropriate database path based on environment"""
    # On Vercel, use /tmp directory (only writable location)
    if os.environ.get('VERCEL'):
        return '/tmp/uniclubs.db'
    return current_app.config.get('DATABASE', 'uniclubs.db')

def get_db():
    """Get database connection from Flask g object"""
    if 'db' not in g:
        db_path = get_db_path()
        g.db = sqlite3.connect(db_path)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    """Close database connection"""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """Initialize database with schema"""
    db = get_db()
    with current_app.open_resource('schema.sql', mode='r') as f:
        db.executescript(f.read())
    db.commit()

def db_exists():
    """Check if database file exists"""
    db_path = get_db_path()
    return os.path.exists(db_path)
