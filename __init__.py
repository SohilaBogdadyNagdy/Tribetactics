from .app import db, create_app
import os
os.environ.setdefault("FLASK_APP", "APP")
db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.
