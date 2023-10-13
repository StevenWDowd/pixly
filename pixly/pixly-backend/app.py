from flask import Flask, request, jsonify
import os
from models import db, connect_db, Photo
from utils import upload_to_s3, create_presigned_url, get_exif_data
from utils import black_white_photo, colorize
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///pixly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

####################### Routes ###################################


@app.post('/photos/add')
def add_photo():
    """Adds a photo"""

    try:
        photo = request.files["user_photo"]

        photo_exif_dict = get_exif_data(photo)
        photo_key = upload_to_s3(photo)
        photo_url = create_presigned_url(photo_key)

        new_photo_entry = Photo(url=photo_url,
                                s3_key=photo_key,
                                gps_info=photo_exif_dict["gps_info"],
                                camera_model=photo_exif_dict["camera_model"],
                                camera_make=photo_exif_dict["camera_make"],
                                image_description=photo_exif_dict["image_description"],
                                date=photo_exif_dict["date"])
        db.session.add(new_photo_entry)
        db.session.commit()

        response = jsonify(new_photo_entry.serialize())
        return (response, 201)

    except (KeyError, IntegrityError):
        response = {"message": "Photo failed to upload"}
        return (jsonify(response), 400)


@app.get('/photos')
def get_all_photos():
    """Get all photos."""

    photos = Photo.query.all()

    serialized_photos = [photo.serialize() for photo in photos]
    return jsonify(serialized_photos)


@app.get('/photos/<int:id>')
def get_photo(id):
    """Get a photo."""

    photo = Photo.query.get_or_404(id)

    serialize_photo = photo.serialize()
    return jsonify(serialize_photo)


@app.post('/photos/search')
def search_photos():
    """Get photos based on a search term."""

    term = request.json["search_term"]

    photos = Photo.query.filter(
        Photo.camera_model.ilike(f'%{term}%') |
        Photo.camera_make.ilike(f'%{term}%') |
        Photo.image_description.ilike(f'%{term}%') |
        Photo.date.ilike(f'%{term}%'))

    serialized_photos = [photo.serialize() for photo in photos]
    return jsonify(serialized_photos)


@app.post('/photos/<int:id>')
def alter_photo(id):
    """Alters photo to grayscale based on user input """

    command = request.json["command"]

    if command == "blackwhite":
        photo = Photo.query.get_or_404(id)
        black_white_photo(photo.s3_key)

    if command == "colorize":
        photo = Photo.query.get_or_404(id)
        colorize(photo.s3_key)

    photo = Photo.query.get_or_404(id)

    serialize_photo = photo.serialize()
    return jsonify(serialize_photo)
