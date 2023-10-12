"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://pbs.twimg.com/profile_images/1237550450/mstom_200x200.jpg"

class User(db.Model):
    """User."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(4000), nullable=False, default= "DEFAULT_IMAGE_URL")

    @property
    def full_name(self):
        """Return the full name"""
        return f"{self.first_name} {self.last_name}"

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)