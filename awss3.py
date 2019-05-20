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
            response = self.s3.upload_file(os.getenv("RELATIVE_PATH_TO_PROJECT_DIRECTORY") + file_name, bucket, object_name)
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
    