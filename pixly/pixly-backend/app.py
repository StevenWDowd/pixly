from flask import Flask, request, jsonify
import boto3
import os
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS
from models import db, connect_db, Photo
from utils import upload_to_s3, create_presigned_url, get_exif_data
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS, cross_origin

#import requests

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000/"], resources=r'/*')
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///pixly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
PUBLIC_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']

connect_db(app)

####################### Routes ###################################
@app.post('/add')
#@cross_origin(allow_headers=['Content-Type'])
def add_photo():
    """Adds a photo"""

    # TODO: secure_filename from werkzerug???
    #TODO: ideas for file-to-S3: temp storage of file in server, manipulating data from form into correct structure
    try:
        photo = request.files["user_photo"]
        print(photo, "photo object")
        print(photo.filename, "photo filename")


        photo_exif_dict = get_exif_data(photo)
        # photo_exif_dict = {
        #     "gps_info": None,
        #     "camera_model": None,
        #     "camera_make": None,
        #     "image_description": None,
        #     "date": None}
        photo_key = upload_to_s3(photo)
        photo_url = create_presigned_url(photo_key)

        new_photo_entry = Photo(url=photo_url,
                                gps_info=photo_exif_dict["gps_info"],
                                camera_model=photo_exif_dict["camera_model"],
                                camera_make=photo_exif_dict["camera_make"],
                                image_description=photo_exif_dict["image_description"],
                                date=photo_exif_dict["date"])
        db.session.add(new_photo_entry)
        db.session.commit()

        return (jsonify(new_photo_entry.serialize()), 201)

    except IntegrityError:
        response = {"message": "Photo failed to upload"}
        return (jsonify(response), 400)

    # massage this data to go into s3
    # massage the data to go into db


#get all photos
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







#EXIF fields to start off: GPSInfo, Make, Model, ImageDescription, DateTime, Software?

#DB Schema: id, {metadata field cols}, url