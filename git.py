import subprocess
#p = subprocess.Popen('cd ../../;ls;', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#for line in p.stdout.readlines():
    #print line,
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
            "git-commit": "git commit -m",
            "git-log": "git log --pretty=oneline --abbrev-commit"
        }
    def _setup_ssh_connection(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_stdin = ssh_stdout = ssh_stderr = None
        try:
            ssh.connect(os.getenv("SSH_ADDRESS"), username=os.getenv("SSH_USERNAME"), password=os.getenv("SSH_PASSWORD"))
            #ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(os.getenv("SSH_TEST_COMMAND"))
        except Exception as e:
            sys.stderr.write("SSH connection error: {0}".format(e).decode('utf-8'))
        if ssh_stdout:
            sys.stdout.write(ssh_stdout.read().decode('utf-8'))
            return ssh
        else:
            return False
    def _output_process(self,process):
        for line in process.stdout.readlines():
            print(line.decode())
    def _run_local_command(self,command):
        process = subprocess.Popen(os.getenv("CHANGE_TO_PROJECT_DIRECTORY")+";"+command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self._output_process(process)
    def status_local(self):
        self._run_local_command(self.commands["git-status"])
    def add_local(self):
        self._run_local_command(self.commands["git-add"])
    def commit_local(self):
        self._run_local_command(self.commands["git-commit"])
    def _log_messages_local(self):
        self._run_local_command(self.commands["git-log"])
    #def push_local(self):
    #def pull_remote(self):
    