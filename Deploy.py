from lib import *
from git import *
from awss3 import *
class Deploy(Git,awss3):
    def __init__(self):
        self.git = Git()
        self.awss3 = awss3()
    def push_to_git(self):
        self.git.pull_local()
        self.git.status_local()
        self.git.add_local()
        self.git.commit_local()
        self.git.push_local()
    def deploy_to_remote_server(self):
        self.git.deploy_to_remote_server()
    def deploy_to_awss3(self,env):
        files_to_upload = self.git.get_added_files() + self.git.get_modified_files()
        files_to_delete = self.git.get_deleted_files()
        files_to_upload = [x for x in files_to_upload if x not in files_to_delete]
        print("-------Files to Upload----")
        print(files_to_upload)
        print("----Files to Delete------")
        print(files_to_delete)
        bucket = os.getenv("TEST_BUCKET")
        #if env == "Prod"
        for filename in files_to_upload:
            self.awss3.upload_file(filename,bucket)
        for filename in files_to_delete:
            self.awss3.delete_file(filename,bucket)
