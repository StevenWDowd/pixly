from flask import Flask, request, jsonify
import boto3
import os
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS
from models import db, connect_db, Photo
from utils import upload_to_s3, create_presigned_url, get_exif_data, black_white_photo
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///pixly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
PUBLIC_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']

connect_db(app)

####################### Routes ###################################


@app.post('/photos/add')
def add_photo():
    """Adds a photo"""

    # TODO: secure_filename from werkzerug???
    # TODO: ideas for file-to-S3: temp storage of file in server, manipulating data from form into correct structure
    try:
        # breakpoint()
        photo = request.files["user_photo"]
        print(photo, "photo object")
        print(photo.filename, "photo filename")

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
        # response.headers.add('Access-Control-Allow-Origin', '*')
        return (response, 201)

    except IntegrityError:
        response = {"message": "Photo failed to upload"}
        return (jsonify(response), 400)

    # massage this data to go into s3
    # massage the data to go into db


# get all photos
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
    print(term, "THIS IS TERM IN BACKEND")
    photos = Photo.query.filter(
        Photo.camera_model.ilike(f'%{term}%') |
        Photo.camera_make.ilike(f'%{term}%') |
        Photo.image_description.ilike(f'%{term}%') |
        Photo.date.ilike(f'%{term}%'))

    serialized_photos = [photo.serialize() for photo in photos]
    return jsonify(serialized_photos)

@app.post('/photos/<int:id>')
def alter_photo(id):
    """Alter photo (color, border) based on user input"""
    command = request.json["command"]
    if command == "blackwhite":
        #func in utils to change photo
        photo = Photo.query.get_or_404(id)
        black_white_photo(photo.s3_key)

    photo = Photo.query.get_or_404(id)
    serialize_photo = photo.serialize()
    return jsonify(serialize_photo)




