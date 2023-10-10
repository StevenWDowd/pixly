from flask import Flask
from dotenv import load_dotenv
import boto3
import os
import requests

EXPIRES_IN_6_DAYS = 518400
SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
PUBLIC_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']

app = Flask(__name__)

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

# if presigned_url is not None:
#     response = requests.get(presigned_url)
#     print("photo url: ", response)