from lib import *
from Remote import *
import boto3
from botocore.exceptions import ClientError
class awss3(Remote):
    def __init__(self):
        if os.getenv("REMOTE_ENV") == "AWS":
            self.s3 = boto3.client('s3')
    #def get_list_of_modified_files
    def upload_file(self,file_name, bucket):
        object_name = file_name
        try:
            response = self.s3.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            print(e)
            return False
        print("FILE" + str(file_name) + "UPLOADED SUCESSFULLY TO BUCKET" + str(bucket))
        return True
    