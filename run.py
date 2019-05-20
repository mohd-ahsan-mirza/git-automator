from lib import *
from Deploy import *
deploy = Deploy()
if os.getenv("REMOTE_ENV") == 'remote-server':
    deploy.push_to_git()
    deploy.deploy_to_remote_server()
    exit()
if os.getenv("REMOTE_ENV") == "AWS":
    print("-----Added files---------")
    deploy.deploy_to_awss3(os.getenv("AWS_ENV"))
    deploy.push_to_git()
    exit()
print("No Remote environment selected")
exit()