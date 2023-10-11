from flask import Flask, request, jsonify
import boto3
import os
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS
from models import db, connect_db, Photo
from utils import upload_to_s3, create_presigned_url, get_exif_data
from sqlalchemy.exc import IntegrityError

#import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///pixly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
PUBLIC_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']

connect_db(app)


#routes:
#add a photo
@app.post('/add')
def add_photo():
    """Adds a photo"""

    # TODO: secure_filename from werkzerug???
    #TODO: ideas for file-to-S3: temp storage of file in server, manipulating data from form into correct structure
    try:
        photo = request.json["url"]
        # photo = request.files["user_photo"]
        print(photo, "from json")


        photo_key = upload_to_s3(photo)
        photo_url = create_presigned_url(photo_key)
        photo_exif_dict = get_exif_data(photo)

        new_photo_entry = Photo(url=photo_url,
                                gps_info=photo_exif_dict["gps_info"],
                                camera_model=photo_exif_dict["camera_model"],
                                camera_make=photo_exif_dict["camera_make"],
                                image_description=photo_exif_dict["image_description"],
                                date=photo_exif_dict["date"])
        db.session.add(new_photo_entry)
        db.session.commit()
        response = {"message": "Photo uploaded"}
        return (jsonify(response), 201)

    except IntegrityError:
        response = {"message": "Photo failed to upload"}
        return (jsonify(response), 400)

    # massage this data to go into s3
    # massage the data to go into db


#get all photos
@app.get('/photos')
def get_all_photos():
    """Get all photos."""
    #query the database for all photos
    # json with list of photos


@app.get('/photos/<int:id>')
def get_photo(id):
    """Get a photo."""
    #query database for photo by id
    #json with info on photo






#EXIF fields to start off: GPSInfo, Make, Model, ImageDescription, DateTime, Software?

#DB Schema: id, {metadata field cols}, url