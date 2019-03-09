from git import *
git = Git()
#git._log_messages_local(true)
#print(git._get_commit_number())
git.status_local()
git.add_local()
git.commit_local()