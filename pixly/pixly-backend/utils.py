import boto3
import os
from dotenv import load_dotenv
from uuid import uuid4
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS

EXPIRES_IN_6_DAYS = 518400
PIXLEY_BUCKET = 'r33-grace-steve-pixly'
SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
PUBLIC_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']

load_dotenv()
#S3 photo storage
s3 = boto3.client(
    "s3",
    "us-east-2",
    aws_access_key_id=PUBLIC_ACCESS_KEY,
    aws_secret_access_key=SECRET_ACCESS_KEY,
)

def create_presigned_url(key):
    """Creates presigned URL for object in s3 bucket"""
    presigned_url = s3.generate_presigned_url(
        ClientMethod="get_object",
        Params={
            "Bucket": PIXLEY_BUCKET,
            "Key": key
    },
    ExpiresIn=EXPIRES_IN_6_DAYS
    )
    return presigned_url

def upload_to_s3(image_file):
    """Uploads an image to S3 storage"""
    new_key = uuid4()

    s3.upload_file(
        image_file,
        PIXLEY_BUCKET,
        new_key,
        ExtraArgs={'ContentType': 'image/jpeg'})
    return new_key

def get_exif_data(image_file):
    """Retrieves EXIF data from an image file, returns a dict. """
    image_exif_dict = {
        "gps_info": None,
        "camera_model": None,
        "camera_make": None,
        "image_description": None,
        "date": None
    }

    #TODO: use load or new with image_file?
    with Image.open(image_file) as img:
        exif_data = img.getexif()
        for tag_id in exif_data:
            tag_name = TAGS.get(tag_id, tag_id)
            value = exif_data.get(tag_id)
            if tag_name == "GPSInfo":
                image_exif_dict["gps_info"] = value
            if tag_name == "Model":
                image_exif_dict["camera_model"] = value
            if tag_name == "Make":
                image_exif_dict["camera_make"] = value
            if tag_name == "ImageDescription":
                image_exif_dict["image_description"] = value
            if tag_name == "DateTime":
                image_exif_dict["date"] = value
    return image_exif_dict





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


#get metadata from an image
# helper functions
    # function to convert date and time string to db compatible date/time str
with Image.open("./canon_hdr_YES.jpg") as test_image:
    sample_exif = test_image.getexif()
    for tag_id in sample_exif:
        tag_name = TAGS.get(tag_id, tag_id)
        value = sample_exif.get(tag_id)
        #print(f'{tag_name},{value}')

# with Image.open("./DSCN0021.jpg") as test_image2:
#     sample_exif = test_image2.getexif()
#     for tag_id in sample_exif:
#         tag_name = TAGS.get(tag_id, tag_id)
#         value = sample_exif.get(tag_id)
#         print(f'{tag_name},{value},{type(value)}')
#         if tag_name == 'DateTime':
#             print('converted date: ', parse(value, yearfirst=True, ignoretz=True))

test_image3 = Image.open("./DSCN0021.jpg")
exif = test_image3.getexif()
print(exif, "EXIF OBJ")
gps_ifd = exif.get_ifd(ExifTags.IFD.GPSInfo)
print(gps_ifd, "GPS DATA")

#GPS_data = sample_exif.get_ifd(ExifTags.TAGS[306])
#print("EXIF data: ", sample_exif)
#print("GPS_data is: ", GPS_data)