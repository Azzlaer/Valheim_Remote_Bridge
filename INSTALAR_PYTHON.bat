@echo off
title Instalador Automatico de Python para Windows 11 x64
setlocal

echo ==========================================
echo   INSTALADOR AUTOMATICO DE PYTHON
echo   Windows 11 x64
echo ==========================================
echo.

:: Version de Python a instalar
set PYTHON_VERSION=3.12.2
set PYTHON_INSTALLER=python-%PYTHON_VERSION%-amd64.exe
set PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%PYTHON_INSTALLER%

:: Carpeta temporal
set TEMP_DIR=%TEMP%\python_installer
mkdir "%TEMP_DIR%" >nul 2>&1

echo Descargando Python %PYTHON_VERSION% (64-bit)...
powershell -Command "Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%TEMP_DIR%\%PYTHON_INSTALLER%'"

if not exist "%TEMP_DIR%\%PYTHON_INSTALLER%" (
    echo ERROR: No se pudo descargar Python.
    pause
    exit /b 1
)

echo.
echo Instalando Python...
"%TEMP_DIR%\%PYTHON_INSTALLER%" ^
 /quiet ^
 InstallAllUsers=1 ^
 PrependPath=1 ^
 Include_test=0

echo.
echo Esperando a que finalice la instalacion...
timeout /t 10 >nul

:: Refrescar variables de entorno
setx PATH "%PATH%" >nul

echo.
echo Verificando instalacion...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no se instalo correctamente.
    pause
    exit /b 1
)

pip --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: pip no funciona correctamente.
    pause
    exit /b 1
)

echo.
echo ==========================================
echo  PYTHON INSTALADO CORRECTAMENTE
echo ==========================================
echo Version de Python:
python --version
echo.
echo Version de pip:
pip --version
echo.
echo Ya puedes usar Python desde cualquier terminal.
echo.

pause
endlocal