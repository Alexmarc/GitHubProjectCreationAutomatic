@echo off

set myProjectName=%1
cd /d %~dp0

@REM python should be an environnement variable
@REM if not you can use the Set_Env_Var.bat to setup it like this :
@REM variable_name=python
@REM variable_value=[your path to your python install, for exemple : C:\Users\username\AppData\Local\Programs\Python\Python36\python.exe]
%python% pyGitHubProjectCreator.py %myProjectName%  