from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""
    app.app_context().push()
    db.app = app
    db.init_app(app)


class Photo(db.Model):
    """Photos in the database."""

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

    s3_key = db.Column(
        db.String,
        nullable=False,
        unique=True
    )

    gps_info = db.Column(
        db.Integer,
        nullable=True
    )

    camera_model = db.Column(
        db.String,
        nullable=True
    )

    camera_make = db.Column(
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

    def serialize(self):
        """Serialize to dictionary."""

        return {
            "id": self.id,
            "url": self.url,
            "s3_key": self.s3_key,
            "gps_info": self.gps_info,
            "camera_model": self.camera_model,
            "camera_make": self.camera_make,
            "image_description": self.image_description,
            "date": self.date
        }
