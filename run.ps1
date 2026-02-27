# Script para ejecutar el servidor FastAPI en Windows
# Uso: .\run.ps1

Write-Host "============================================"
Write-Host "Sistema de Agendamiento de Citas - FastAPI"
Write-Host "============================================"
Write-Host ""

# Verificar si Python está instalado
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python encontrado: $pythonVersion"
} catch {
    Write-Host "✗ Error: Python no está instalado o no está en PATH"
    Write-Host "Descárgalo desde: https://www.python.org/downloads/"
    exit 1
}

# Verificar si el entorno virtual existe
if (Test-Path ".\.venv\Scripts\Activate.ps1") {
    Write-Host "✓ Entorno virtual encontrado"
    Write-Host "Activando entorno virtual..."
    & ".\.venv\Scripts\Activate.ps1"
} else {
    Write-Host "⚠ Entorno virtual no encontrado"
    Write-Host "Crear uno con: python -m venv .venv"
}

# Verificar si FastAPI está instalado
try {
    $fastApiCheck = pip show fastapi 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ FastAPI está instalado"
    } else {
        throw "FastAPI no instalado"
    }
} catch {
    Write-Host "✗ FastAPI no está instalado"
    Write-Host "Instálalo con: pip install -r requirements.txt"
    exit 1
}

# Iniciar el servidor
Write-Host ""
Write-Host "═══════════════════════════════════════════"
Write-Host "Iniciando servidor en http://localhost:8000"
Write-Host "═══════════════════════════════════════════"
Write-Host ""
Write-Host "Presiona CTRL+C para detener el servidor"
Write-Host ""

uvicorn main:app --reload --host 0.0.0.0 --port 8000

