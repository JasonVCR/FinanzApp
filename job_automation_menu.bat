@echo off
REM Job Automation System - Quick Start
REM This script provides easy access to all automation functions

:menu
cls
echo =====================================================
echo         JOB AUTOMATION SYSTEM - QUICK START
echo =====================================================
echo.
echo Current time: %date% %time%
echo.
echo 1. Run automation once (test)
echo 2. Start automated scheduler (9:00 AM and 7:00 PM daily)
echo 3. Test system components
echo 4. View latest job results
echo 5. Preview email design
echo 6. Test email sending
echo 7. Setup Windows Service
echo 8. Install/Update dependencies
echo 9. Configure email settings
echo 10. Exit
echo.
set /p choice="Enter your choice (1-10): "

if "%choice%"=="1" goto run_once
if "%choice%"=="2" goto start_scheduler
if "%choice%"=="3" goto test_system
if "%choice%"=="4" goto view_results
if "%choice%"=="5" goto preview_email
if "%choice%"=="6" goto test_email
if "%choice%"=="7" goto setup_service
if "%choice%"=="8" goto install_deps
if "%choice%"=="9" goto config_email
if "%choice%"=="10" goto exit
goto menu

:run_once
echo.
echo Running automation once...
echo.
"C:/Users/vladi/Desktop/CODEX/venv/App financiera/.venv/Scripts/python.exe" simple_automation.py
echo.
echo Automation completed. Press any key to return to menu...
pause >nul
goto menu

:start_scheduler
echo.
echo Starting automated scheduler...
echo This will run the job search at 9:00 AM and 7:00 PM daily
echo Press Ctrl+C to stop the scheduler
echo.
"C:/Users/vladi/Desktop/CODEX/venv/App financiera/.venv/Scripts/python.exe" simple_scheduler.py
echo.
echo Scheduler stopped. Press any key to return to menu...
pause >nul
goto menu

:test_system
echo.
echo Testing system components...
echo.
"C:/Users/vladi/Desktop/CODEX/venv/App financiera/.venv/Scripts/python.exe" simple_scheduler.py test
echo.
echo Test completed. Press any key to return to menu...
pause >nul
goto menu

:view_results
echo.
echo Opening job applications folder...
echo.
if exist "job_applications" (
    explorer job_applications
) else (
    echo No job applications found yet. Run the automation first.
)
echo.
echo Press any key to return to menu...
pause >nul
goto menu

:setup_service
echo.
echo Setting up Windows Service...
echo This requires administrator privileges.
echo.
call setup_windows_service.bat
echo.
echo Press any key to return to menu...
pause >nul
goto menu

:install_deps
echo.
echo Installing/updating dependencies...
echo.
"C:/Users/vladi/Desktop/CODEX/venv/App financiera/.venv/Scripts/pip.exe" install -r requirements.txt
echo.
echo Dependencies updated. Press any key to return to menu...
pause >nul
goto menu

:config_email
echo.
echo Email Configuration Help
echo ========================
echo.
echo To enable email reports:
echo 1. Enable 2-factor authentication in Gmail
echo 2. Generate App Password in Google Account settings
echo 3. Edit .env file with your credentials
echo.
echo Opening .env file for editing...
if exist ".env" (
    notepad .env
) else (
    echo .env file not found. Creating from template...
    copy .env.template .env
    notepad .env
)
echo.
echo Email configuration complete. Press any key to return to menu...
pause >nul
goto menu

:preview_email
echo.
echo Generating email design preview...
echo.
"C:/Users/vladi/Desktop/CODEX/venv/App financiera/.venv/Scripts/python.exe" test_email_design.py
echo.
echo Press any key to return to menu...
pause >nul
goto menu

:test_email
echo.
echo Testing email sending with beautiful design...
echo.
"C:/Users/vladi/Desktop/CODEX/venv/App financiera/.venv/Scripts/python.exe" test_beautiful_email.py
echo.
echo Press any key to return to menu...
pause >nul
goto menu

:exit
echo.
echo Thank you for using the Job Automation System!
echo.
exit /b 0
