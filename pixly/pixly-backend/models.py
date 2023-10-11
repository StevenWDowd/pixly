from flask_sqlalchemy import SQLAlchemy
#from app import app
db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    app.app_context().push()
    db.app = app
    db.init_app(app)

class Photo(db.Model):
    """Photos in the system."""

    __tablename__ = "photos"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    url = db.Column(
        db.String,
        nullable=False,
        unique=True
    )

    gps_info = db.Column(
        db.Integer,
        nullable=True
    )

    camera_model= db.Column(
        db.String,
        nullable=True
    )

    camera_make= db.Column(
        db.String,
        nullable=True
    )

    image_description = db.Column(
        db.String,
        nullable=True
    )

    date = db.Column(
        db.String,
        nullable=True
    )