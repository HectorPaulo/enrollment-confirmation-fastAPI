"""
Script para probar la API del sistema de agendamiento de citas
"""

import requests
import json
from datetime import datetime, timedelta

# URL base de la API
BASE_URL = "http://localhost:8000"

def test_formulario_cita():
    """Prueba la creación de una cita"""

    # Datos de prueba
    fecha_futura = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

    cita_data = {
        "nombre": "Test Usuario",
        "email": "test@example.com",
        "fecha": fecha_futura,
        "hora": "14:30",
        "descripcion": "Esta es una cita de prueba para validar el sistema"
    }

    print("📋 Enviando cita de prueba...")
    print(f"Datos: {json.dumps(cita_data, indent=2)}")

    try:
        response = requests.post(
            f"{BASE_URL}/citas/agendar",
            json=cita_data
        )

        print(f"\n✅ Status Code: {response.status_code}")

        if response.status_code == 200:
            resultado = response.json()
            print(f"✅ Cita agendada exitosamente!")
            print(f"ID de la cita: {resultado['id']}")
            print(f"Respuesta: {json.dumps(resultado, indent=2)}")
        else:
            print(f"❌ Error: {response.json()}")

    except Exception as e:
        print(f"❌ Error de conexión: {str(e)}")
        print("\n💡 Asegúrate de que el servidor esté ejecutándose:")
        print("   uvicorn main:app --reload")


def test_listar_citas():
    """Prueba la obtención de todas las citas"""

    print("\n📋 Obteniendo lista de citas...")

    try:
        response = requests.get(f"{BASE_URL}/citas")

        print(f"\n✅ Status Code: {response.status_code}")

        if response.status_code == 200:
            citas = response.json()
            print(f"✅ Se obtuvieron {len(citas)} citas")
            if citas:
                print(f"Respuesta: {json.dumps(citas, indent=2)}")
            else:
                print("(No hay citas agendadas aún)")
        else:
            print(f"❌ Error: {response.json()}")

    except Exception as e:
        print(f"❌ Error de conexión: {str(e)}")


def test_pagina_principal():
    """Prueba que la página principal esté disponible"""

    print("\n🌐 Verificando página principal...")

    try:
        response = requests.get(f"{BASE_URL}/")

        print(f"\n✅ Status Code: {response.status_code}")

        if response.status_code == 200:
            if "index.html" in response.text or "Agendar Cita" in response.text:
                print("✅ Página principal disponible")
            else:
                print("⚠️  Se recibió una respuesta pero podría no ser la página esperada")
        else:
            print(f"❌ Error: {response.status_code}")

    except Exception as e:
        print(f"❌ Error de conexión: {str(e)}")


if __name__ == "__main__":
    print("=" * 50)
    print("🧪 PRUEBAS DEL SISTEMA DE AGENDAMIENTO DE CITAS")
    print("=" * 50)

    test_pagina_principal()
    test_formulario_cita()
    test_listar_citas()

    print("\n" + "=" * 50)
    print("✅ Pruebas completadas")
    print("=" * 50)

