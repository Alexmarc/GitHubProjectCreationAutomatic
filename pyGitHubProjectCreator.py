import sys
import os
from github import Github
from pathlib import Path
import time
import shutil
import subprocess  # Utilisé pour ouvrir le fichier avec VS Code


foldername = input("Please enter the folder name: ")

time.sleep(1)

path = Path(os.environ.get('mp'))         # add projects dirctory to the env vars like you did with Set_Env_Var.bat
token = os.environ.get('gt')        # add github token to the env vars like you did with Set_Env_Var.bat / see https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token to know how to create a token
_dir = path / foldername



def CreateLocalFolder():
    _dir.mkdir(parents=True, exist_ok=True)
    os.chdir(str(_dir))

    print(f'{foldername} created locally')


def CreateReadmeFile():
    script_path = Path(__file__).resolve()
    current_directory = os.path.dirname(script_path)
    source_path =  os.path.join(current_directory, "ReadmeExemple.md")
    destination_path = os.path.join(_dir, "README.md")

    shutil.copy2(source_path, destination_path)

    time.sleep(1)

    #Open README.md in vscode
    # subprocess.run(["code", str(destination_path)])


def CreateOnlineRepo():
    g = Github(token)
    user = g.get_user()
    login = user.login
    repo = user.create_repo(foldername, private=True)



    commands = ['git init',
                f'git remote add origin https://github.com/{login}/{foldername}.git',
                'git add .',
                'git commit -m "Initial commit"',
                'git push -u origin main']

    for c in commands:
        os.system(c)

    print("Repository github created ")
    time.sleep(1)


CreateLocalFolder()
CreateReadmeFile()
CreateOnlineRepo()

