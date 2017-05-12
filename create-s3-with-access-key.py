#!/usr/bin/env python3
from boto3.session import Session

access_key = ''
secret_access_key=''

session = Session(aws_access_key_id=access_key,aws_secret_access_key=secret_access_key)

s3 = session.resource('s3')

s3.create_bucket(Bucket='thisisanewbucketforme123456')

for bucket in s3.buckets.all():
    print(bucket.name)
