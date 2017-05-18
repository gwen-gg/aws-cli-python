#!/usr/bin/env python3
from boto3.session import Session
import config

access_key = ''
secret_access_key=''
region_name='eu-west-1'

session = Session(aws_access_key_id=access_key,aws_secret_access_key=secret_access_key,region_name=region_name)

s3 = session.resource('s3')

s3.create_bucket(Bucket='blacknodelabs.com',CreateBucketConfiguration={ 'LocationConstraint': region_name})
s3.create_bucket(Bucket='www.blacknodelabs.com', CreateBucketConfiguration={ 'LocationConstraint': region_name})

for bucket in s3.buckets.all():
    print(bucket.name)
