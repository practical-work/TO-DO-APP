# Model definitions for the Flask application

from app import db  # Import the SQLAlchemy instance from the app package

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each task
    title = db.Column(db.String(100), nullable=False)  # Title of the task, cannot be null
    status = db.Column(db.String(20), nullable=False, default='pending')  # Status of the task, default is 'pending'
