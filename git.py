from lib import *
#Import package
from remoteServer import *
class Git(remoteServer):
    def __init__(self):
        #Initiate base classes
        remoteServer.__init__(self)
        self.commands = {
            "git-status":"git status",
            "git-add":"git add .",
            "git-commit": "git commit -m ",
            "git-log": "git log --pretty=oneline --abbrev-commit",
            "git-push": "git push origin",
            "git-pull": "git pull origin",
            "git-modified-files": "git diff --name-only",
            "git-add-files": "git ls-files --others --exclude-standard",
            "git-deleted-files": "git ls-files --deleted",
            "directory-list":"ls",
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
    def _convert_shell_output_to_list(self,result):
        resultArray = []
        for filename in result.stdout.readlines():
            resultArray.append(filename.decode().strip("\n"))
        return resultArray
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
    def get_added_files(self,output=False):
        result = self._run_local_command(self.commands["git-add-files"],output)
        return self._convert_shell_output_to_list(result)
    def get_modified_files(self,output=False):
        result =  self._run_local_command(self.commands["git-modified-files"],output)
        return self._convert_shell_output_to_list(result)
    def get_deleted_files(self,output=False):
        result = self._run_local_command(self.commands["git-deleted-files"],output)
        return self._convert_shell_output_to_list(result)



    