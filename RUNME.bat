@echo off

REM Get the current directory of the batch file
set script_dir=%~dp0

REM Define the path to the requirements.txt file
set requirements_file=%script_dir%requirements.txt

REM Define the command to install the dependencies
set install_command=pip install -r %requirements_file%

REM Run the command to install the dependencies
echo Installing dependencies...
%install_command%
echo Dependencies installed successfully.

echo Now you can run the EXE

pause