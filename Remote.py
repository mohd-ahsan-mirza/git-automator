from lib import *
class Remote:
    def retrieve_password(self,description,value):
        print(description)
        return subprocess.check_output(os.getenv("PASSWORD_RETRIEVAL_COMMAND") + " -get " + str(value) + " --return-value",shell=True).decode("utf-8").strip("\n")

