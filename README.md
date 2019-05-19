# Description
This tool automates git add, commit, push on a local machine and pull on a remote server or cloud(AWS). I built this tool to avoid copy pasting changes to my personal site

# Local

Add the following line in .gitignore
```
git-automator/
```
Pull this project into your desired repository on your machine

[Pull this repository](https://github.com/mohd-ahsan-mirza/redis-local-encryptor)

Add the absolute path of ``` run.py ``` as value of ``` PASSWORD_RETRIEVAL_COMMAND ``` in .env file
### Make sure git-automator doesn't get commited to your git repo
Add ```git-automator/``` in .gitignore

Copy the .env.template to .env and fill out the mandatory fields in the file

Make sure the repo on github has been created

It is recommeded that you make the first commit manually with message "Commit 1"

Make sure the repo has been initialized and pulled on both local and remote server

Make sure the remote origin url is set with password
```
https://USERNAME:PASS@github.com/USERNAME/REPONAME.git
```

# Remote Server
Set the upstream branch
```
git push --set-upstream origin master
```

# AWS
Configure AWS account on your CLI using ```aws configure```
```
pip3 install boto3
```
In your AWS account create a test and a production bucket

Add those bucket names in the .env file

# Notes
If you are adding any files directly on github please follow the commit message convention
### Warning: If there are multiple people modifying the same branch this automator might not work
