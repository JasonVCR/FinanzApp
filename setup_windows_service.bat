@echo off
REM Windows Service Setup for Job Automation System
REM This script helps set up the job automation as a Windows service

echo Job Automation System - Windows Service Setup
echo =============================================
echo.

REM Check if running as administrator
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: This script must be run as Administrator
    echo Right-click on the script and select "Run as administrator"
    pause
    exit /b 1
)

REM Change to script directory
cd /d "%~dp0"

REM Check if NSSM is available (Non-Sucking Service Manager)
where nssm >nul 2>&1
if %errorlevel% neq 0 (
    echo NSSM not found. Installing NSSM...
    echo.
    echo Please download NSSM from https://nssm.cc/download
    echo Extract nssm.exe to a folder in your PATH or to this directory
    echo Then run this script again.
    pause
    exit /b 1
)

REM Service configuration
set SERVICE_NAME=JobAutomationService
set SERVICE_DISPLAY_NAME=Job Automation System
set SERVICE_DESCRIPTION=Automated job search and CV generation system
set PYTHON_PATH=C:\Users\vladi\Desktop\CODEX\venv\App financiera\.venv\Scripts\python.exe
set SCRIPT_PATH=%~dp0simple_scheduler.py

echo Setting up Windows Service...
echo Service Name: %SERVICE_NAME%
echo Display Name: %SERVICE_DISPLAY_NAME%
echo Python Path: %PYTHON_PATH%
echo Script Path: %SCRIPT_PATH%
echo.

REM Check if service already exists
sc query %SERVICE_NAME% >nul 2>&1
if %errorlevel% equ 0 (
    echo Service already exists. Removing existing service...
    nssm stop %SERVICE_NAME%
    nssm remove %SERVICE_NAME% confirm
    timeout /t 2 /nobreak >nul
)

REM Install the service
echo Installing service...
nssm install %SERVICE_NAME% "%PYTHON_PATH%" "%SCRIPT_PATH%"

REM Configure service
echo Configuring service...
nssm set %SERVICE_NAME% DisplayName "%SERVICE_DISPLAY_NAME%"
nssm set %SERVICE_NAME% Description "%SERVICE_DESCRIPTION%"
nssm set %SERVICE_NAME% Start SERVICE_AUTO_START
nssm set %SERVICE_NAME% AppDirectory "%~dp0"
nssm set %SERVICE_NAME% AppStdout "%~dp0logs\service_stdout.log"
nssm set %SERVICE_NAME% AppStderr "%~dp0logs\service_stderr.log"
nssm set %SERVICE_NAME% AppRotateFiles 1
nssm set %SERVICE_NAME% AppRotateOnline 1
nssm set %SERVICE_NAME% AppRotateSeconds 86400
nssm set %SERVICE_NAME% AppRotateBytes 10485760

REM Create logs directory
if not exist "logs" mkdir logs

REM Start the service
echo Starting service...
nssm start %SERVICE_NAME%

REM Check service status
timeout /t 3 /nobreak >nul
sc query %SERVICE_NAME% | find "RUNNING" >nul
if %errorlevel% equ 0 (
    echo.
    echo ✓ Service installed and started successfully!
    echo.
    echo Service Information:
    echo - Name: %SERVICE_NAME%
    echo - Display Name: %SERVICE_DISPLAY_NAME%
    echo - Status: Running
    echo - Logs: %~dp0logs\
    echo.
    echo The service will automatically start job automation at 9:00 AM and 7:00 PM daily.
    echo.
    echo To manage the service:
    echo - Start: nssm start %SERVICE_NAME%
    echo - Stop: nssm stop %SERVICE_NAME%
    echo - Remove: nssm remove %SERVICE_NAME%
    echo - Status: sc query %SERVICE_NAME%
    echo.
) else (
    echo.
    echo ✗ Service installation failed or service is not running
    echo Check the logs in %~dp0logs\ for error details
    echo.
)

echo Setup complete!
pause
