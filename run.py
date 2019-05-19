from lib import *
from Deploy import *
deploy = Deploy()
deploy.push_to_git()
if os.getenv("REMOTE_ENV") == 'remote-server':
    deploy.deploy_to_remote_server()
    exit()
print("No Remote environment selected")
exit()