# Description
This tool automates git add, commit, push on a local machine and pull on a remote server or cloud(AWS). I built this tool to avoid copy pasting changes to my personal site

# Local

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

# Notes
If you are adding any files directly on github please follow the commit message convention
### Warning: If there are multiple people modifying the same branch this automator might not work
