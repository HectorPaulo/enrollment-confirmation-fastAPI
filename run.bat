@echo off
REM Script para ejecutar el servidor FastAPI en Windows

echo.
echo ============================================
echo Sistema de Agendamiento de Citas - FastAPI
echo ============================================
echo.

REM Activar el entorno virtual si existe
if exist .venv\Scripts\activate.bat (
    echo Activando entorno virtual...
    call .venv\Scripts\activate.bat
)

REM Ejecutar el servidor
echo.
echo Iniciando servidor en http://localhost:8000
echo Presiona CTRL+C para detener el servidor
echo.

uvicorn main:app --reload

pause

