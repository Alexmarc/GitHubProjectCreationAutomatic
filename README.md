"# Automatic GitHub project creator" 

### Base on:
```
https://www.youtube.com/watch?v=7Y8Ppin12r4&list=PL5tVJtjoxKzq87h9k4AwjXG-AKYpyvMWC&index=4

Thanks to Kalle Hallden for the orginal idea

```

### Description:
```
Create automaticaly a GitHub project and a local folder for you to start working.
You won't need to setup the projects like this :
git init
git add origin https...

You'll just have to double click on CreateProject.bat setup a project name and VOILA !
```


### Initial Setup:
```
Get the project but zip or with git url :
git clone "https://github.com/Alexmarc/GitHubProjectCreationAutomatic.git"
cd ProjectInitializationAutomation
pip install -r requirements.txt (will install PyGithub library)

Put the CreateProject.bat file at the root of your workspace.
Setup the right paths in files :
- CreateProject.bat
- create.bat

To create environments variables you can use the script Set_Env_Var.bat setting a key and a value.
```


### Usage:
```
Run "CreateProject.bat", set a project name.

```