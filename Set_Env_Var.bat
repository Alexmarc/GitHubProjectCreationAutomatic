set /p variable_name=Enter variable name:
set /p variable_value=Enter variable value:

@REM start cmd /k setx variable_name variable_value
setx %variable_name% %variable_value%

pause