#!/usr/bin/env python3
"""
📋 REFERENCIA RÁPIDA - Sistema de Agendamiento de Citas
Este script muestra un resumen de la implementación
"""

import os
from datetime import datetime

def mostrar_header():
    print("\n" + "="*70)
    print("  🎯 SISTEMA DE AGENDAMIENTO DE CITAS - REFERENCIA RÁPIDA")
    print("="*70 + "\n")

def mostrar_instrucciones():
    print("🚀 PARA EJECUTAR LA APLICACIÓN:\n")
    print("  Opción 1 - En Windows:")
    print("    → Doble clic en: run_dev.bat\n")
    print("  Opción 2 - En línea de comandos:")
    print("    → python -m uvicorn main:app --reload\n")
    print("  ✅ Luego abre: http://localhost:8000\n")

def mostrar_instalacion():
    print("📦 INSTALACIÓN INICIAL:\n")
    print("  1. python -m venv .venv")
    print("  2. .venv\\Scripts\\activate  (Windows)")
    print("  3. pip install -r requirements.txt")
    print("  4. Crear archivo .env con datos SMTP\n")

def mostrar_archivos():
    print("📁 ARCHIVOS PRINCIPALES:\n")
    archivos = {
        "main.py": "Rutas FastAPI (GET /, POST /citas/agendar, etc)",
        "config.py": "Configuración (nombres, URLs, validaciones)",
        "models/__init__.py": "Modelos Pydantic (Cita, CitaResponse)",
        "utils/storage.py": "Gestión de citas.json",
        "utils/email_service.py": "Envío de emails SMTP",
        "static/index.html": "Aplicación web (formulario + listado)",
        "citas.json": "Base de datos local (auto-generada)",
        ".env": "Variables de entorno SMTP (debes crear)",
    }

    for archivo, descripcion in archivos.items():
        print(f"  • {archivo:<30} → {descripcion}")
    print()

def mostrar_rutas_api():
    print("🌐 ENDPOINTS API:\n")
    rutas = [
        ("GET", "/", "Página principal (HTML)"),
        ("POST", "/citas/agendar", "Crear cita + enviar email"),
        ("GET", "/citas", "Obtener todas las citas (JSON)"),
        ("GET", "/citas/confirmar/{id}", "Confirmar cita por email"),
        ("GET", "/citas/ver", "Página de listado alternativa"),
    ]

    for metodo, ruta, descripcion in rutas:
        print(f"  {metodo:<6} {ruta:<30} → {descripcion}")
    print()

def mostrar_env_template():
    print("🔐 TEMPLATE DE .env (copiar y rellenar):\n")
    env_content = """SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_EMAIL=tu_email@gmail.com
SMTP_PASSWORD=tu_contraseña_app"""
    print(env_content)
    print("\n  ℹ️  La contraseña debe ser de APLICACIÓN, no la contraseña de Gmail\n")

def mostrar_validaciones():
    print("✅ VALIDACIONES IMPLEMENTADAS:\n")
    validaciones = {
        "Nombre": "Requerido, 3-100 caracteres",
        "Email": "Formato válido con @ y punto",
        "Fecha": "Futura, no puede ser hoy o anterior",
        "Hora": "Formato HH:MM",
        "Descripción": "Mínimo 10, máximo 500 caracteres",
    }

    for campo, validacion in validaciones.items():
        print(f"  • {campo:<15} → {validacion}")
    print()

def mostrar_estructura_cita():
    print("📊 ESTRUCTURA DE CITA EN JSON:\n")
    estructura = """{
  "id": "uuid-único",
  "nombre": "Juan Pérez",
  "email": "juan@example.com",
  "fecha": "2024-03-20",
  "hora": "14:30",
  "descripcion": "Consulta de servicios",
  "creada_en": "2024-02-25T10:30:00.000000",
  "confirmada": false,
  "confirmada_en": null
}"""
    print(estructura)
    print()

def mostrar_flujo():
    print("🔄 FLUJO DE TRABAJO:\n")
    pasos = [
        "1️⃣  Usuario abre http://localhost:8000",
        "2️⃣  Completa formulario en 'Agendar Cita'",
        "3️⃣  Hace clic en 'Agendar Cita'",
        "4️⃣  Backend valida y guarda en citas.json",
        "5️⃣  Envía email con enlace de confirmación",
        "6️⃣  Usuario hace clic en email",
        "7️⃣  Cita se marca como 'Confirmada'",
        "8️⃣  Admin ve estado actualizado en 'Ver Citas'",
    ]

    for paso in pasos:
        print(f"  {paso}")
    print()

def mostrar_documentacion():
    print("📚 DOCUMENTACIÓN DISPONIBLE:\n")
    docs = {
        "SETUP.md": "Instalación y configuración",
        "GUIA_RAPIDA.md": "Preguntas frecuentes",
        "DIAGRAMA_FLUJO.md": "Diagramas técnicos",
        "DOCUMENTACION_TECNICA.md": "Detalles completos",
        "http://localhost:8000/docs": "API docs automática (Swagger)",
    }

    for archivo, descripcion in docs.items():
        print(f"  • {archivo:<35} → {descripcion}")
    print()

def mostrar_errores_comunes():
    print("⚠️  ERRORES COMUNES Y SOLUCIONES:\n")
    errores = {
        "No llega el email": "- Verifica .env\n                          - Usa contraseña de APP, no de Gmail",
        "Fecha inválida": "- Solo fechas futuras\n                          - Formato YYYY-MM-DD",
        "Puerto 8000 en uso": "- Usa puerto 8001: --port 8001",
        "El .env no se detecta": "- Crea en raíz (mismo nivel que main.py)\n                          - Reinicia la app",
    }

    for error, solucion in errores.items():
        print(f"  ❌ {error}")
        print(f"     ✅ {solucion}\n")

def mostrar_checklist():
    print("✔️  CHECKLIST PRE-LANZAMIENTO:\n")
    checklist = [
        "[ ] Archivo .env creado y configurado",
        "[ ] requirements.txt instalado (pip install -r)",
        "[ ] Entorno virtual activado",
        "[ ] Puerto 8000 disponible",
        "[ ] Credenciales SMTP válidas",
        "[ ] Prueba: agendar una cita",
        "[ ] Prueba: recibir email",
        "[ ] Prueba: confirmar por email",
        "[ ] Prueba: ver cita en listado",
    ]

    for item in checklist:
        print(f"  {item}")
    print()

def mostrar_shortcuts():
    print("⌨️  ATAJOS ÚTILES:\n")
    shortcuts = [
        ("Ctrl+C", "Detener servidor"),
        ("Ctrl+R", "Recargar página en navegador"),
        ("F12", "Abrir DevTools (ver errores)"),
        ("http://localhost:8000/docs", "Ver API en Swagger"),
        ("python -m uvicorn main:app --reload --port 8001", "Cambiar puerto"),
    ]

    for atajo, descripcion in shortcuts:
        print(f"  • {atajo:<50} → {descripcion}")
    print()

def mostrar_footer():
    print("="*70)
    print(f"  Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("  Versión: 1.0")
    print("  Estado: ✅ Implementación Completada")
    print("="*70 + "\n")

if __name__ == "__main__":
    mostrar_header()
    mostrar_instrucciones()
    mostrar_instalacion()
    mostrar_archivos()
    mostrar_rutas_api()
    mostrar_env_template()
    mostrar_validaciones()
    mostrar_estructura_cita()
    mostrar_flujo()
    mostrar_documentacion()
    mostrar_errores_comunes()
    mostrar_checklist()
    mostrar_shortcuts()
    mostrar_footer()

    print("💡 PRÓXIMA ACCIÓN: Crear archivo .env y ejecutar run_dev.bat\n")

