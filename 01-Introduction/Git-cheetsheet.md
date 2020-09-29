# Git Cheetsheet

These command should be executed from MacOs or Linux terminal, for windows users please run it from git bash.

To clone a repo from the server, run

```bash
git clone [address]
```

> This will create a new folder with the repo name

Then you may add changes to the repo, Then to add a "snapshot" create a commit

```bash
git add .
git commit -m [message]
```

> git add . prepares all files to be commited

> Please add a descriptive commit message after -m flag, such as "added bug fix for main.py"

Then if you want to push all the commit to the server, run:

```bash
git push
```

> Git may ask you password in this step, please provide the password for your github account

Sometimes in the future, your repo in github may have more commits that the one on your local computer, this may be caused by someone contributing or you push changes from other machine, to refresh you local repo and get latest changes, please run:

```bash
git pull
```


