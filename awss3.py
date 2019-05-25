from lib import *
from Remote import *
import boto3
from botocore.exceptions import ClientError
class awss3(Remote):
    def __init__(self):
        if os.getenv("REMOTE_ENV") == "AWS":
            self.s3 = boto3.client('s3')    
    def upload_file(self,file_name, bucket):
        object_name = file_name
        try:
            response = self.s3.put_object(
                ACL ='public-read',
                Body = open(os.getenv("RELATIVE_PATH_TO_PROJECT_DIRECTORY") + file_name,"r").read(),
                Bucket = bucket,
                Key = object_name,
                CacheControl="max-age=0,no-cache,no-store,must-revalidate",
                ContentType="text/"+splitext(file_name)[1].strip("."),
            )
        except ClientError as e:
            print(e)
            return False
        print("FILE" + str(file_name) + " UPLOADED SUCESSFULLY TO BUCKET " + str(bucket))
        return True
    def delete_file(self,file_name,bucket):
        try:
            self.s3.delete_object(Bucket=bucket, Key=file_name)
        except ClientError as e:
            print(e)
            return False
        print("FILE" + str(file_name) + " DELETED SUCESSFULLY TO BUCKET " + str(bucket))
    