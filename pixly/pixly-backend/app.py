from flask import Flask, request, jsonify
import boto3
import os
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS
from models import db, connect_db, Photo
from utils import upload_to_s3, create_presigned_url, get_exif_data

#import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///pixly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


#routes:
#add a photo
@app.post('/add')
def add_photo():
    """Adds a photo"""

    # formdata
    #TODO: put this in try/except block
    try
    photo = request.files["user_photo"]
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
    # massage this data to go into s3

    # create a key for s3
    # get the url back from s3
    # extract metadata from photo
    # massage the data to go into db

    # Photo(photo_url, gps_info, camera_make, camera_model, image_description, date)
    #sumbit to database

    # json back to front end- {message: success to upload photo, statuscode: 201}

#get all photos
@app.get('/photos')
def get_all_photos():
    """Get all photos."""
    #query the database for all photos
    # json with list of photos


@app.get('/photos/<in:id>')
def get_photo(id):
    """Get a photo."""
    #query database for photo by id
    #json with info on photo






#EXIF fields to start off: GPSInfo, Make, Model, ImageDescription, DateTime, Software?

#DB Schema: id, {metadata field cols}, url