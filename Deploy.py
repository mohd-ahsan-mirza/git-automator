from lib import *
from git import *
from awss3 import *
class Deploy(Git,awss3):
    def __init__(self):
        self.git = Git()
    def push_to_git(self):
        self.git.pull_local()
        self.git.status_local()
        self.git.add_local()
        self.git.commit_local()
        self.git.push_local()
    def deploy_to_remote_server(self):
        self.git.deploy_to_remote_server()
