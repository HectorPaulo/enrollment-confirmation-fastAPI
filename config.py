# Configuración de la Aplicación FastAPI

# Información de la Empresa (personalizable)
EMPRESA_NOMBRE = "Mi Empresa"
EMPRESA_TELEFONO = "+1 (555) 123-4567"
EMPRESA_EMAIL = "contacto@miempresa.com"

# URL base de la app (para enlaces de confirmación)
APP_BASE_URL = "http://localhost:8000"

# Configuración de citas
FECHA_MINIMA_DIAS_ADELANTE = 1  # Mínimo de días para agendar citas
HORA_INICIO_ATENCION = "09:00"   # Hora de inicio de atención
HORA_CIERRE_ATENCION = "17:00"   # Hora de cierre de atención

# Configuración de validación
DESCRIPCION_MIN_CARACTERES = 10
DESCRIPCION_MAX_CARACTERES = 500
NOMBRE_MIN_CARACTERES = 3
NOMBRE_MAX_CARACTERES = 100

# Almacenamiento
ARCHIVO_CITAS = "citas.json"

# Logging
LOG_NIVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
