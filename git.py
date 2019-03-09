import subprocess
import paramiko
import sys
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Git:
    def __init__(self):
        self.ssh = self._setup_ssh_connection()
        self.commands = {
            "git-status":"git status",
            "git-add":"git add .",
            "git-commit": "git commit -m ",
            "git-log": "git log --pretty=oneline --abbrev-commit",
            "git-push": "git push origin",
            "directory-list":"ls",
            "git-pull": "git pull origin"
        }
        self.commit_numbers = []
        for line in self._log_messages_local().stdout.readlines():
            self.commit_numbers.append(line.decode().split()[-1])
    def _setup_ssh_connection(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_stdin = ssh_stdout = ssh_stderr = None
        try:
            ssh.connect(os.getenv("SSH_ADDRESS"), username=os.getenv("SSH_USERNAME"), password=os.getenv("SSH_PASSWORD"))
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(os.getenv("SSH_TEST_COMMAND"))
        except Exception as e:
            sys.stderr.write("SSH connection error: {0}".format(e).decode('utf-8'))
        if ssh_stdout:
            #sys.stdout.write(ssh_stdout.read().decode('utf-8'))
            return ssh
        else:
            return False
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
    def _run_remote_command(self,command,output=True):
        ssh_stdin = ssh_stdout = ssh_stderr = None
        command = os.getenv("CHANGE_TO_REMOTE_DIRECTORY")+";"+command
        try:
            ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(command)
        except Exception as e:
            sys.stderr.write("SSH connection error: {0}".format(e).decode('utf-8'))
        if ssh_stdout:
            if(output):
                print("---------------------------")
                print("Command --> "+command)
                print("---------------------------")
                sys.stdout.write(ssh_stdout.read().decode('utf-8'))
                print("---------------------------")
                return
            else:
                return sys.stdout
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
    def pull_remote(self):
        return self._run_remote_command(self.commands["git-pull"]+" "+os.getenv("WORKING_BRANCH"))

    