from flask import Flask
from dotenv import load_dotenv
import boto3
import os


SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
PUBLIC_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']


app = Flask(__name__)

load_dotenv()

# s3 = boto3.client('s3')

s3 = boto3.client(
    "s3",
    "us-east-2",
    aws_access_key_id=PUBLIC_ACCESS_KEY,
    aws_secret_access_key=SECRET_ACCESS_KEY,
)


response = s3.list_buckets()

for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

result = s3.upload_file('./as-above-so-below.jpg', 'r33-grace-steve-pixly', 'test-jpg')

print('result is: ', result)
