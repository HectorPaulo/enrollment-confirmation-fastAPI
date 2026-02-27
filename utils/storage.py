import json
import os
from datetime import datetime
from uuid import uuid4
from typing import List, Dict, Optional


CITAS_FILE = "citas.json"


def _normalizar_cita(cita: Dict) -> Dict:
    cita.setdefault("confirmada", False)
    cita.setdefault("confirmada_en", None)
    return cita


def cargar_citas() -> List[Dict]:
    """Carga todas las citas del archivo JSON"""
    if not os.path.exists(CITAS_FILE):
        return []
    try:
        with open(CITAS_FILE, "r", encoding="utf-8") as f:
            citas = json.load(f)
            return [_normalizar_cita(c) for c in citas]
    except (json.JSONDecodeError, IOError):
        return []


def guardar_citas(citas: List[Dict]) -> None:
    """Guarda las citas en el archivo JSON"""
    with open(CITAS_FILE, "w", encoding="utf-8") as f:
        json.dump(citas, f, indent=2, ensure_ascii=False)


def agregar_cita(nombre: str, email: str, fecha: str, hora: str, descripcion: str) -> Dict:
    """Agrega una nueva cita y retorna la cita creada"""
    citas = cargar_citas()

    nueva_cita = {
        "id": str(uuid4()),
        "nombre": nombre,
        "email": email,
        "fecha": fecha,
        "hora": hora,
        "descripcion": descripcion,
        "creada_en": datetime.now().isoformat(),
        "confirmada": False,
        "confirmada_en": None
    }

    citas.append(nueva_cita)
    guardar_citas(citas)

    return nueva_cita


def obtener_citas() -> List[Dict]:
    """Obtiene todas las citas"""
    return cargar_citas()


def obtener_cita_por_id(cita_id: str) -> Optional[Dict]:
    """Obtiene una cita específica por ID"""
    citas = cargar_citas()
    for cita in citas:
        if cita["id"] == cita_id:
            return _normalizar_cita(cita)
    return None


def confirmar_cita(cita_id: str) -> Optional[Dict]:
    """Marca una cita como confirmada y retorna la cita actualizada"""
    citas = cargar_citas()
    for cita in citas:
        if cita["id"] == cita_id:
            if not cita.get("confirmada"):
                cita["confirmada"] = True
                cita["confirmada_en"] = datetime.now().isoformat()
                guardar_citas(citas)
            return _normalizar_cita(cita)
    return None


def eliminar_cita(cita_id: str) -> bool:
    """Elimina una cita por ID"""
    citas = cargar_citas()
    citas_filtradas = [c for c in citas if c["id"] != cita_id]

    if len(citas_filtradas) < len(citas):
        guardar_citas(citas_filtradas)
        return True
    return False
