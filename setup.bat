@echo off
echo ========================================
echo    AI Quiz Generator Setup Script
echo ========================================
echo.

echo Setting up environment...
set GEMINI_API_KEY=AIzaSyCnn4Art8B1Uog0zRcOethbzkkJo4tyzAg

echo Installing dependencies...
py -m pip install -r backend/requirements.txt

echo Creating .env file...
echo GEMINI_API_KEY=AIzaSyCnn4Art8B1Uog0zRcOethbzkkJo4tyzAg > .env

echo Starting the application...
echo.
echo ========================================
echo    Application is starting...
echo    Open your browser and go to:
echo    http://localhost:3000
echo ========================================
echo.
echo Press Ctrl+C to stop the application
echo.

py main.py

pause 