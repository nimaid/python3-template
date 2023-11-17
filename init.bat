@echo off

REM Run this file to initialize the project

set ORIGDIR="%CD%"
set FILEDIR="%~dp0"

set INSTALLCONDA="install_conda_windows.bat"
set SELFNAME="init.bat"

cd %FILEDIR%

REM Install conda
call cmd /c %INSTALLCONDA%
if errorlevel 1 goto ERROR

REM Run init.py
call conda activate base
if errorlevel 1 goto ERROR
call pip install keyboard
if errorlevel 1 goto ERROR
call python init.py
if errorlevel 1 goto ERROR

REM Install the current conda environment
call conda env create -f environment.yml
if errorlevel 1 goto ERROR

REM Delete the init files
del /f /q %INSTALLCONDA% 1>nul 2>&1
del /f /q %SELFNAME% 1>nul 2>&1

cd %ORIGDIR%

:ERROR
echo Project initialization failed!
exit /B 1

:DONE
echo Project initialization done!
exit /B 0