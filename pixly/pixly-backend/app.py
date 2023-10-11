from flask import Flask
from dotenv import load_dotenv
import boto3
import os
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS
#from models import db, connect_db
from datetime import date
from dateutil.parser import parse

#import requests

EXPIRES_IN_6_DAYS = 518400
SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
PUBLIC_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
#     "DATABASE_URL", 'postgresql:///pixly')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True

# connect_db(app)

load_dotenv()

#S3 photo storage
s3 = boto3.client(
    "s3",
    "us-east-2",
    aws_access_key_id=PUBLIC_ACCESS_KEY,
    aws_secret_access_key=SECRET_ACCESS_KEY,
)

our_bucket = 'r33-grace-steve-pixly'
test_pic_key = 'test-jpg2'

# gets all buckets
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

#uploads an image to a known bucket
result = s3.upload_file(
    './as-above-so-below.jpg',
    our_bucket,
    test_pic_key,
    ExtraArgs= {'ContentType': 'image/jpeg'})

print('result is: ', result)

#get AWS image URL
presigned_url = s3.generate_presigned_url(
    ClientMethod="get_object",
    Params={
        "Bucket": our_bucket,
        "Key": test_pic_key
    },
    ExpiresIn=EXPIRES_IN_6_DAYS
)
print(presigned_url, "presignedURL")

with Image.open("./canon_hdr_YES.jpg") as test_image:
    sample_exif = test_image.getexif()
    for tag_id in sample_exif:
        tag_name = TAGS.get(tag_id, tag_id)
        value = sample_exif.get(tag_id)
        #print(f'{tag_name},{value}')

with Image.open("./DSCN0021.jpg") as test_image2:
    sample_exif = test_image2.getexif()
    for tag_id in sample_exif:
        tag_name = TAGS.get(tag_id, tag_id)
        value = sample_exif.get(tag_id)
        print(f'{tag_name},{value},{type(value)}')
        if tag_name == 'DateTime':
            print('converted date: ', parse(value, yearfirst=True, ignoretz=True))

    #GPS_data = sample_exif.get_ifd(ExifTags.TAGS[306])
    #print("EXIF data: ", sample_exif)
    #print("GPS_data is: ", GPS_data)

# if presigned_url is not None:
#     response = requests.get(presigned_url)
#     print("photo url: ", response)

#EXIF fields to start off: GPSInfo, Make, Model, ImageDescription, DateTime, Software?

#DB Schema: id, {metadata field cols}, url