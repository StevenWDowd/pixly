import boto3
import os
from dotenv import load_dotenv
from uuid import uuid4
from PIL import Image, ImageOps
from PIL.ExifTags import TAGS
from tempfile import NamedTemporaryFile

load_dotenv()

EXPIRES_IN_6_DAYS = 518400
PIXLEY_BUCKET = 'r33-grace-steve-pixly'
SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
PUBLIC_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']

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

    new_key = str(uuid4())

    s3.upload_fileobj(
        image_file,
        PIXLEY_BUCKET,
        new_key,
        ExtraArgs={'ContentType': 'image/jpeg'})

    return new_key


def get_exif_data(image_file):
    """Retrieves EXIF data from an image file, returns a dict of EXIF data."""

    image_exif_dict = {
        "gps_info": None,
        "camera_model": None,
        "camera_make": None,
        "image_description": None,
        "date": None
    }

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
        image_file.seek(0)

    return image_exif_dict


def black_white_photo(key):
    """Changes photo based on key to grayscale."""

    with NamedTemporaryFile(suffix=".jpg", delete=False) as temp:
        s3.download_file(PIXLEY_BUCKET, key, temp.name)

        with Image.open(temp.name) as t:
            gray_scale = t.convert("L")
            gray_scale.save(temp.name)

            oriented = ImageOps.exif_transpose(gray_scale)
            oriented.save(temp.name)

            s3.upload_file(
                temp.name,
                PIXLEY_BUCKET,
                key,
                ExtraArgs={'ContentType': 'image/jpeg'})

def colorize(key):
    """Changes photo based on key to RGB color version."""

    with NamedTemporaryFile(suffix=".jpg", delete=False) as temp:
        s3.download_file(PIXLEY_BUCKET, key, temp.name)

        with Image.open(temp.name) as t:
            color_photo = t.convert("RGB")
            color_photo.save(temp.name)

            oriented = ImageOps.exif_transpose(color_photo)
            oriented.save(temp.name)

            s3.upload_file(
                temp.name,
                PIXLEY_BUCKET,
                key,
                ExtraArgs={'ContentType': 'image/jpeg'})
