@echo off
echo ========================================
echo    AI Quiz Generator - Backup Script
echo ========================================
echo.

echo Creating backup of current working state...
echo.

REM Create backup directory with timestamp
set TIMESTAMP=%date:~-4,4%-%date:~-10,2%-%date:~-7,2%_%time:~0,2%-%time:~3,2%-%time:~6,2%
set TIMESTAMP=%TIMESTAMP: =0%
set BACKUP_DIR=ai-quiz-generator-backup-%TIMESTAMP%

echo Creating backup directory: %BACKUP_DIR%
mkdir %BACKUP_DIR%

echo Copying project files...
xcopy /E /I /Y main.py %BACKUP_DIR%\
xcopy /E /I /Y backend %BACKUP_DIR%\backend\
xcopy /E /I /Y frontend %BACKUP_DIR%\frontend\
xcopy /E /I /Y setup.bat %BACKUP_DIR%\
xcopy /E /I /Y run.bat %BACKUP_DIR%\
xcopy /E /I /Y README.md %BACKUP_DIR%\
xcopy /E /I /Y .env %BACKUP_DIR%\

echo.
echo ========================================
echo    Backup Complete!
echo ========================================
echo.
echo Backup location: %BACKUP_DIR%
echo.
echo To restore this backup:
echo 1. Copy all files from %BACKUP_DIR% to a new folder
echo 2. Run setup.bat in the new folder
echo.
pause 