# AI Quiz Generator - PowerShell Start Script

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "    AI Quiz Generator" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Set environment variable
$env:GEMINI_API_KEY = "AIzaSyCnn4Art8B1Uog0zRcOethbzkkJo4tyzAg"

Write-Host "Environment configured..." -ForegroundColor Green
Write-Host ""

Write-Host "========================================" -ForegroundColor Yellow
Write-Host "    Starting Application..." -ForegroundColor Yellow
Write-Host "    Open your browser and go to:" -ForegroundColor Yellow
Write-Host "    http://localhost:3000" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press Ctrl+C to stop the application" -ForegroundColor Red
Write-Host ""

# Start the application
py main.py 