from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional


class Cita(BaseModel):
    nombre: str
    email: str
    fecha: str  # Formato: YYYY-MM-DD
    hora: str   # Formato: HH:MM
    descripcion: str

    @field_validator('email')
    def validar_email(cls, v):
        if '@' not in v or '.' not in v:
            raise ValueError('Email inválido')
        return v

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Juan Pérez",
                "email": "juan@example.com",
                "fecha": "2024-03-15",
                "hora": "14:30",
                "descripcion": "Consulta de servicios"
            }
        }


class CitaResponse(BaseModel):
    id: str
    nombre: str
    email: str
    fecha: str
    hora: str
    descripcion: str
    creada_en: str
    confirmada: bool
    confirmada_en: Optional[str]
