@echo off
REM Installation and Run Script for Portfolio Website

echo ========================================
echo Portfolio Website - Installation Script
echo ========================================
echo.

REM Check if Node.js is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Node.js not found. Installing...
    echo.
    echo Please download and install Node.js from:
    echo https://nodejs.org/en/download
    echo.
    echo After installation, close this window and run this script again.
    pause
    exit /b 1
) else (
    echo ✓ Node.js found
    node --version
    echo.
)

REM Install dependencies
echo Installing dependencies...
call npm install

if %errorlevel% neq 0 (
    echo Error during npm install
    pause
    exit /b 1
)

echo.
echo ========================================
echo Starting Development Server...
echo ========================================
echo.
echo Your website will be available at:
echo http://localhost:3000
echo.
echo Press Ctrl+C to stop the server
echo.

REM Run development server
call npm run dev

pause
