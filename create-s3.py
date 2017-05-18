#!/usr/bin/env python3
import boto3
import config

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

s3.create_bucket(Bucket='blacknodelabs.com')
s3.create_bucket(Bucket='www.blacknodelabs.com')