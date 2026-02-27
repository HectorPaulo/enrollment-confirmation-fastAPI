@echo off
REM Script para ejecutar la aplicación FastAPI de Citas

echo.
echo ╔══════════════════════════════════════════════════════════╗
echo ║     Sistema de Agendamiento de Citas - FastAPI          ║
echo ╚══════════════════════════════════════════════════════════╝
echo.

REM Verificar si el entorno virtual está activado
if not exist ".venv\Scripts\activate.bat" (
    echo ERROR: Entorno virtual no encontrado.
    echo Por favor, crea el entorno virtual primero:
    echo   python -m venv .venv
    echo   .venv\Scripts\activate
    echo   pip install -r requirements.txt
    pause
    exit /b 1
)

REM Activar entorno virtual
call .venv\Scripts\activate.bat

echo ✓ Entorno virtual activado
echo.

REM Verificar si .env existe
if not exist ".env" (
    echo ⚠️  ADVERTENCIA: Archivo .env no encontrado
    echo.
    echo Debes crear un archivo .env con las siguientes variables:
    echo.
    echo   SMTP_SERVER=smtp.gmail.com
    echo   SMTP_PORT=587
    echo   SMTP_EMAIL=tu_email@gmail.com
    echo   SMTP_PASSWORD=tu_contrasena_app
    echo.
    echo Para más información, revisa GUIA_RAPIDA.md
    echo.
    pause
)

echo.
echo 🚀 Iniciando servidor...
echo.
echo URL: http://localhost:8000
echo Documentación: http://localhost:8000/docs
echo.
echo Presiona CTRL+C para detener el servidor
echo.

REM Iniciar la aplicación
python -m uvicorn main:app --reload

pause

