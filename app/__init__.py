from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
# Initialize the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)  # Initialize the Flask application
    app.config['SECRET_KEY'] = 'my-secret-key' # Set a secret key for session management and security
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "sqlite:///todo.db"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Disable the event system for performance
    db.init_app(app) # Initialize the database with the Flask application

    from app.routes.auth import auth_bp  # Import the authentication blueprint
    from app.routes.tasks import task_bp  # Import the todo blueprint
    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)

    return app  # Return the Flask application instance

