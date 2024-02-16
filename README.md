"# Automatic GitHub project creator" 

A Python script to help create a GitHub repository online and locally, it's made to save time on repository creation.

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
Get the project by zip or with git url :
git clone "https://github.com/Alexmarc/GitHubProjectCreationAutomatic.git"

You need to install GitHub dependancy for python : pip install -r requirements.txt (will install PyGithub library)

```


### Usage:
```

It's really easy to use :
- Setup a "mp" environnement variable that target your workspace
- Setup a "gt" environment variable for your GitHub token (see https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- Then run the script, select a name for your repository (local directory will be named like the online one)
- It's done your PRIVATE repo is created, if you need a public one just delete "privet=true" inside create_repo function

Njoy


```
