from lib import *
from Deploy import *
deploy = Deploy()
deploy.push_to_git()
if os.getenv("REMOTE_ENV") == 'remote-server':
    deploy.deploy_to_remote_server()
    exit()
if os.getenv("REMOTE_ENV") == "AWS":
    print("-----Added files---------")
    print(deploy.deploy_to_awss3())
    exit()
print("No Remote environment selected")
exit()