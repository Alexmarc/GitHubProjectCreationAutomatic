import sys
import os
from github import Github
from pathlib import Path
import time

foldername = str(sys.argv[1])

time.sleep(1)

path = os.environ.get('mp')         # add projects dirctory to the env vars like you did with Set_Env_Var.bat
token = os.environ.get('gt')        # add github token to the env vars like you did with Set_Env_Var.bat / see https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token to know how to create a token
_dir = path + '/' + foldername

g = Github(token)
user = g.get_user()
login = user.login
repo = user.create_repo(foldername)

commands = [f'echo "# {repo.name}" >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{foldername}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

print("Repository github created start create local one")
print("Local folder path : " + _dir)

time.sleep(1)

os.mkdir(_dir)
os.chdir(_dir)

for c in commands:
    os.system(c)

print(f'{foldername} created locally')