@echo off
REM SecureML Cloud - Windows Development Setup Script
REM Run this script to set up the development environment on Windows

echo.
echo ============================================
echo   SecureML Cloud - Windows Setup
echo ============================================
echo.

REM Check for Docker
echo [1/5] Checking for Docker...
docker --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Docker is not installed or not in PATH
    echo Please install Docker Desktop from: https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)
echo OK: Docker is installed
echo.

REM Check for Node.js
echo [2/5] Checking for Node.js...
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js from: https://nodejs.org/
    pause
    exit /b 1
)
echo OK: Node.js is installed
for /f "tokens=*" %%i in ('node --version') do set NODE_VERSION=%%i
echo Version: %NODE_VERSION%
echo.

REM Setup backend environment
echo [3/5] Setting up backend...
cd backend
if not exist .env (
    echo Creating .env file...
    copy .env.example .env
    echo WARNING: Please edit backend\.env with your configuration
)
cd ..
echo OK: Backend ready
echo.

REM Setup frontend dependencies
echo [4/5] Installing frontend dependencies...
cd frontend
if not exist node_modules (
    echo Installing npm packages...
    call npm install
    if errorlevel 1 (
        echo ERROR: Failed to install npm packages
        pause
        exit /b 1
    )
) else (
    echo OK: Dependencies already installed
)
cd ..
echo.

REM Start Docker services
echo [5/5] Starting Docker services...
echo.
docker-compose up -d
if errorlevel 1 (
    echo ERROR: Failed to start Docker services
    echo Make sure Docker Desktop is running
    pause
    exit /b 1
)
echo.
echo ============================================
echo   ✓ Setup completed successfully!
echo ============================================
echo.
echo Services are starting...
timeout /t 10
echo.
echo.
echo 📍 Services will be available at:
echo    - Frontend: http://localhost:3000
echo    - Backend API: http://localhost:8000
echo    - API Documentation: http://localhost:8000/docs
echo    - PostgreSQL: localhost:5432
echo    - Redis: localhost:6379
echo.
echo 🔐 Test Login Credentials:
echo    - Email: test@secureml.com
echo    - Password: Test@1234
echo.
echo 📝 Next steps:
echo    1. Open terminal and run: cd frontend && npm run dev
echo    2. Visit http://localhost:3000
echo    3. Login with test credentials above
echo.
echo 🛑 To stop services:
echo    - Run: docker-compose down
echo.
pause
