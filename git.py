from lib import *
from remoteServer import *
class Git(remoteServer):
    def __init__(self):
        self.commands = {
            "git-status":"git status",
            "git-add":"git add .",
            "git-commit": "git commit -m ",
            "git-log": "git log --pretty=oneline --abbrev-commit",
            "git-push": "git push origin",
            "directory-list":"ls",
            "git-pull": "git pull origin" # Remote Server
        }
        self.commit_numbers = []
        for line in self._log_messages_local().stdout.readlines():
            self.commit_numbers.append(line.decode().split()[-1])
    def _output_process(self,process):
        for line in process.stdout.readlines():
            print(line.decode())
    def _run_local_command(self,command,output=True):
        command = os.getenv("CHANGE_TO_PROJECT_DIRECTORY")+";"+command
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if(output):
            print("---------------------------")
            print("Command --> "+command)
            print("---------------------------")
            self._output_process(process)
            print("---------------------------")
            return
        else:
            return process
    def _get_commit_message(self):
        if len(self.commit_numbers)!=0 and self.commit_numbers[0].isdigit():
            return "'Commit " + str((int(self.commit_numbers[0])+1)) + "'"
        else:
            return "'Commit 1'"
    def _log_messages_local(self,output=False):
        return self._run_local_command(self.commands["git-log"],output)
    def status_local(self):
        return self._run_local_command(self.commands["git-status"])
    def add_local(self):
        return self._run_local_command(self.commands["git-add"])
    def commit_local(self):
        return self._run_local_command(self.commands["git-commit"]+str(self._get_commit_message()))
    def push_local(self):
        return self._run_local_command(self.commands["git-push"]+" "+os.getenv("WORKING_BRANCH"))
    def pull_local(self):
        return self._run_local_command(self.commands["git-pull"]+" "+os.getenv("WORKING_BRANCH"))

    