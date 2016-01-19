# -*- coding=utf-8 -*-
#!/bin/env python

import boto3
from include.tools import fprint

class S3Api(object):
    def __init__(self):
        self.s3_resource = boto3.resource('s3')
        self.s3_client = boto3.client('s3')
    def __all__(self):
        return (list_buckets, create_bucket)
    def list_buckets(self):
        return self.s3_client.list_buckets()
    def create_bucket(self,bucket,**kwargs):
        print kwargs
        return  self.s3_client.create_bucket(Bucket=bucket,**kwargs)
    def get_bucket_acl(self, bucket):
        return self.s3_client.get_bucket_acl(Bucket=bucket)
    def delete_bucket(self, bucket):
        return self.s3_client.delete_bucket(Bucket=bucket)
    '''
    @path : file path
    @backet : bucket name
    @name : s3 object name 
    '''
    def upload_file(self, path, backet, name):
        return self.s3_client.upload_file(path, backet, name)
    def list_objects(self,bucket, **kwargs):
        return self.s3_client.list_objects(Bucket=bucket, **kwargs)
    def get_object_acl(self, bucket, obj, **kwargs):
        return self.s3_client.get_object_acl(Bucket=bucket, Key=obj, **kwargs)

if __name__ == '__main__':
    api = S3Api()
    fprint( api.list_buckets() )
    #api.create_bucket("lonay11220",**{'ACL':'public-read'})
    #print api.get_bucket_acl("lonay11220")
    #api.upload_file("f1.txt","lonay11220","f1.txt")
    #print api.list_objects("lonay11220",**{"Marker":"f1"})
    #print api.get_object_acl("lonay11220","f1.txt")