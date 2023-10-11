from flask_sqlalchemy import SQLAlchemy
#from app import app
db = SQLAlchemy()

# def connect_db(app):
#     """Connect to database."""
#     app.app_context().push()
#     db.app = app
#     db.init_app(app)

# class Photo(db.Model){
#     __tablename__ = "photos"

#     id = db.Column(
#         db.Integer,
#         primary_key=True,
#         autoincrement=True
#     )

#     url = db.Column(
#         db.String,
#         nullable=False
#     )

#     gps_info = db.Column(
#         db.Integer
#     )
# }

