@echo off
REM Job Automation Scheduler Startup Script
REM This script starts the job automation system

echo Starting Job Automation System...
echo Current time: %date% %time%

REM Change to the script directory
cd /d "%~dp0"

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if required files exist
if not exist "final_automation.py" (
    echo ERROR: final_automation.py not found
    pause
    exit /b 1
)

if not exist "robust_scheduler.py" (
    echo ERROR: robust_scheduler.py not found
    pause
    exit /b 1
)

if not exist "config.json" (
    echo ERROR: config.json not found
    pause
    exit /b 1
)

REM Install requirements if needed
echo Installing/updating requirements...
pip install -r requirements.txt

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo Creating .env file from template...
    copy ".env.template" ".env"
    echo Please edit .env file with your actual credentials
    pause
)

REM Start the scheduler
echo Starting scheduler...
python robust_scheduler.py

REM If we get here, scheduler stopped
echo Scheduler stopped. Press any key to exit...
pause
