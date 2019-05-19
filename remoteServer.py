from lib import *
from Remote import *
class remoteServer(Remote):
    def __init__(self):
        self.ssh = self._setup_ssh_connection()
    def _setup_ssh_connection(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_stdin = ssh_stdout = ssh_stderr = None
        try:
            ssh.connect(os.getenv("SSH_ADDRESS"), username=os.getenv("SSH_USERNAME"), password=self.retrieve_password("Retrieving password for server","private-server"))
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(os.getenv("SSH_TEST_COMMAND"))
        except Exception as e:
            sys.stderr.write("SSH connection error: {0}".format(e).decode('utf-8'))
        if ssh_stdout:
            #sys.stdout.write(ssh_stdout.read().decode('utf-8'))
            return ssh
        else:
            return False
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
    def deploy_to_remote_server(self):
        return self._run_remote_command("git pull origin "+os.getenv("WORKING_BRANCH"))
