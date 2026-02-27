from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from datetime import datetime
import os

from models import Cita, CitaResponse
from utils.storage import agregar_cita, obtener_citas, confirmar_cita
from utils.email_service import enviar_email_confirmacion
from config import EMPRESA_NOMBRE, APP_BASE_URL

app = FastAPI(title="Sistema de Agendamiento de Citas")

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    """Sirve la página principal con el formulario"""
    return FileResponse("static/index.html", media_type="text/html")


@app.get("/citas/ver")
async def ver_citas():
    """Sirve la página para ver las citas creadas"""
    return FileResponse("static/citas.html", media_type="text/html")


@app.post("/citas/agendar", response_model=CitaResponse)
async def agendar_cita(cita: Cita):
    """
    Endpoint para agendar una nueva cita.

    - Valida los datos recibidos
    - Guarda la cita como PENDIENTE DE CONFIRMACIÓN en el almacenamiento
    - Envía un email con enlace para que el usuario confirme

    La cita solo se considera confirmada después de que el usuario
    haga clic en el enlace de confirmación del email.
    """
    try:
        # Validar que la fecha sea válida y futura
        fecha_cita = datetime.strptime(cita.fecha, "%Y-%m-%d")
        if fecha_cita.date() < datetime.now().date():
            raise HTTPException(
                status_code=400,
                detail="La fecha de la cita no puede ser en el pasado"
            )

        # Guardar la cita (inicialmente sin confirmar)
        cita_guardada = agregar_cita(
            nombre=cita.nombre,
            email=cita.email,
            fecha=cita.fecha,
            hora=cita.hora,
            descripcion=cita.descripcion
        )

        confirm_url = f"{APP_BASE_URL}/citas/confirmar/{cita_guardada['id']}"

        # Enviar email de confirmación con el enlace
        enviar_email_confirmacion(
            destinatario=cita.email,
            nombre_cliente=cita.nombre,
            fecha=cita.fecha,
            hora=cita.hora,
            descripcion=cita.descripcion,
            empresa_nombre=EMPRESA_NOMBRE,
            confirm_url=confirm_url
        )

        return CitaResponse(**cita_guardada)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Formato de datos inválido: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al agendar la cita: {str(e)}"
        )


@app.get("/citas", response_model=list[CitaResponse])
async def listar_citas():
    """
    Endpoint para listar todas las citas (útil para administración).
    En producción, deberías agregar autenticación.
    """
    citas = obtener_citas()
    return [CitaResponse(**cita) for cita in citas]


@app.get("/citas/confirmar/{cita_id}")
async def confirmar_cita_email(cita_id: str):
    """
    Endpoint para confirmar una cita mediante el enlace del email.
    Solo marca la cita como confirmada cuando el usuario hace clic en el enlace.
    """
    cita = confirmar_cita(cita_id)
    if not cita:
        html = """
        <html>
            <head>
                <meta charset="UTF-8" />
                <title>Error - Cita no encontrada</title>
                <style>
                    body { font-family: Arial, sans-serif; padding: 40px; }
                    .error { color: #d32f2f; }
                </style>
            </head>
            <body>
                <h2 class="error">❌ Error: Cita no encontrada</h2>
                <p>No pudimos encontrar la cita solicitada. Verifica que el enlace sea correcto.</p>
            </body>
        </html>
        """
        return HTMLResponse(content=html, status_code=404)

    html = f"""
    <html>
        <head>
            <meta charset="UTF-8" />
            <title>Cita confirmada</title>
            <style>
                body {{ font-family: Arial, sans-serif; padding: 40px; background-color: #f9f9f9; }}
                .container {{ max-width: 600px; margin: 0 auto; background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
                .success {{ color: #2e7d32; }}
                .details {{ background-color: #f5f5f5; padding: 15px; border-left: 4px solid #2e7d32; margin: 20px 0; }}
                .button {{ display: inline-block; padding: 10px 20px; background-color: #2e7d32; color: white; text-decoration: none; border-radius: 4px; margin-top: 20px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2 class="success">✅ Tu cita ha sido confirmada</h2>
                <p>¡Excelente! Tu cita ha sido confirmada correctamente.</p>
                
                <div class="details">
                    <p><strong>Detalles de tu cita:</strong></p>
                    <p><strong>Nombre:</strong> {cita['nombre']}</p>
                    <p><strong>Fecha:</strong> {cita['fecha']}</p>
                    <p><strong>Hora:</strong> {cita['hora']}</p>
                    <p><strong>Descripción:</strong> {cita['descripcion']}</p>
                </div>
                
                <p>Te esperamos en la fecha y hora indicadas. Si necesitas cambiar o cancelar, por favor contacta con nosotros.</p>
                
                <a href="/" class="button">Volver al inicio</a>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html)


@app.get("/hello/{name}")
async def say_hello(name: str):
    """Endpoint de ejemplo"""
    return {"message": f"Hello {name}"}
