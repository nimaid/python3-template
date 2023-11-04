@echo off

set MAINFAILENAME=python3-template
set ENVNAME=%MAINFAILENAME%

set ORIGDIR=%CD%
set DISTDIR=%ORIGDIR%\dist
set BUILDDIR=%ORIGDIR%\build

set PY=%ORIGDIR%\%MAINFAILENAME%.py
set SPEC=%ORIGDIR%\%MAINFAILENAME%.spec
set EXE=%DISTDIR%\%MAINFAILENAME%.exe

echo Building portable EXE...
call conda run -n %ENVNAME% pyinstaller ^
    --clean ^
    --noconfirm ^
	--add-data icon.png;. ^
    --onefile ^
    --icon=icon.ico ^
    "%PY%"
if errorlevel 1 goto ERROR

echo Cleaning up before making release...
move "%EXE%" "%ORIGDIR%"
del /f /s /q "%DISTDIR%" 1>nul 2>&1
rmdir /s /q "%DISTDIR%" 1>nul 2>&1
del /f /s /q "%BUILDDIR%" 1>nul 2>&1
rmdir /s /q "%BUILDDIR%" 1>nul 2>&1
del /f /q "%SPEC%" 1>nul 2>&1

goto DONE


:ERROR
cd %ORIGDIR%
echo Portable EXE build failed!
exit /B 1

:DONE
cd %ORIGDIR%
echo Portable EXE build done!
exit /B 0