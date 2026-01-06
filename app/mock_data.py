from app.database import get_db
from werkzeug.security import generate_password_hash

def insert_mock_data():
    db = get_db()
    
    # Insert users
    users = [
        ('admin', 'admin@example.com', generate_password_hash('admin123'), 'Admin'),
        ('executive', 'exec@example.com', generate_password_hash('exec123'), 'Club Executive'),
        ('member', 'member@example.com', generate_password_hash('member123'), 'General Member'),
        ('user2', 'user2@example.com', generate_password_hash('pass123'), 'General Member'),
    ]
    db.executemany('INSERT OR IGNORE INTO users (username, email, password_hash, role) VALUES (?, ?, ?, ?)', users)
    
    # Insert clubs
    clubs = [
        ('Computer Science Club', 'A club for CS enthusiasts', 2),  # executive id 2
        ('Art Club', 'Express your creativity', None),
        ('Sports Club', 'Stay active and fit', None),
    ]
    db.executemany('INSERT OR IGNORE INTO clubs (name, description, executive_id) VALUES (?, ?, ?)', clubs)
    
    # Insert memberships
    memberships = [
        (3, 1),  # member joins CS Club
        (4, 1),  # user2 joins CS Club
        (3, 2),  # member joins Art Club
    ]
    db.executemany('INSERT OR IGNORE INTO memberships (user_id, club_id) VALUES (?, ?)', memberships)
    
    # Insert events
    events = [
        (1, 'Coding Workshop', 'Learn Python basics', '2025-12-01 10:00:00'),
        (1, 'Hackathon', '24-hour coding challenge', '2025-12-15 09:00:00'),
        (2, 'Art Exhibition', 'Showcase your art', '2025-11-30 14:00:00'),
    ]
    db.executemany('INSERT OR IGNORE INTO events (club_id, title, description, event_date) VALUES (?, ?, ?, ?)', events)
    
    db.commit()