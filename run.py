from lib import *
from git import *
git = Git()
#git._log_messages_local(true)
#print(git._get_commit_number())
git.pull_local()
git.status_local()
git.add_local()
git.commit_local()
git.push_local()
if os.getenv("REMOTE_ENV") == 'remote-server':
    git.deploy_to_remote_server()
    exit()
print("No Remote environment selected")
exit()