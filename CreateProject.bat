set /p projectName=Enter project name:
echo "Project name will be : " %projectName%

pause

start cmd /k "Setup your path to this file 'create.bat' " %projectName%