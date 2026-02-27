import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
from typing import Optional

load_dotenv()


def enviar_email_confirmacion(
    destinatario: str,
    nombre_cliente: str,
    fecha: str,
    hora: str,
    descripcion: str,
    empresa_nombre: str = "Mi Empresa",
    confirm_url: str | None = None
) -> bool:
    """
    Envía un email de confirmación de cita.

    Requiere variables de entorno:
    - SMTP_SERVER
    - SMTP_PORT
    - SMTP_EMAIL
    - SMTP_PASSWORD
    """

    try:
        smtp_server = os.getenv("SMTP_SERVER")
        smtp_port = int(os.getenv("SMTP_PORT", "587"))
        smtp_email = os.getenv("SMTP_EMAIL")
        smtp_password = os.getenv("SMTP_PASSWORD")

        # Validar que tenemos las credenciales
        if not all([smtp_server, smtp_email, smtp_password]):
            print("⚠️ Variables SMTP no configuradas en .env")
            return False

        # Crear mensaje
        mensaje = MIMEMultipart("alternative")
        mensaje["Subject"] = f"Confirmación de Cita - {empresa_nombre}"
        mensaje["From"] = smtp_email
        mensaje["To"] = destinatario

        # Cuerpo del email en HTML
        enlace_confirmacion_html = ""
        if confirm_url:
            enlace_confirmacion_html = (
                f"<div style=\"background-color: #fff3cd; padding: 15px; border-left: 4px solid #ffc107; margin: 20px 0;\">"
                f"<p style=\"color: #856404; font-weight: bold;\">⚠️ ACCIÓN REQUERIDA</p>"
                f"<p style=\"color: #856404;\">Tu cita aún está <strong>pendiente de confirmación</strong>. "
                f"Debes hacer clic en el botón de abajo para confirmar tu cita.</p>"
                f"</div>"
                f"<p style=\"text-align: center;\">"
                f"<a href=\"{confirm_url}\" "
                f"style=\"display:inline-block;padding:12px 24px;background:#0066cc;"
                f"color:#fff;text-decoration:none;border-radius:4px;font-weight:bold;\">"
                f"✅ Confirmar mi cita</a>"
                f"</p>"
            )

        cuerpo_html = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px; background-color: #f9f9f9; border-radius: 8px;">
                    <h2 style="color: #0066cc;">Tu cita ha sido registrada</h2>
                    
                    <p>¡Hola <strong>{nombre_cliente}</strong>!</p>
                    
                    <p>Gracias por agendar una cita con nosotros. A continuación, encontrarás los detalles de tu cita:</p>
                    
                    <div style="background-color: #ffffff; padding: 15px; border-left: 4px solid #0066cc; margin: 20px 0;">
                        <p><strong>Empresa:</strong> {empresa_nombre}</p>
                        <p><strong>Fecha:</strong> {fecha}</p>
                        <p><strong>Hora:</strong> {hora}</p>
                        <p><strong>Descripción:</strong> {descripcion}</p>
                    </div>

                    {enlace_confirmacion_html}
                    
                    <p style="color: #666; margin-top: 20px;">Si necesitas cambiar o cancelar tu cita, por favor responde a este email.</p>
                    
                    <hr style="border: none; border-top: 1px solid #ddd; margin: 20px 0;">
                    
                    <p style="color: #999; font-size: 12px;">
                        Este es un email automático. Por favor no respondas directamente a este correo.
                    </p>
                </div>
            </body>
        </html>
        """

        # Cuerpo del email en texto plano
        enlace_confirmacion_texto = f"\n⚠️ ACCIÓN REQUERIDA: Debes confirmar tu cita haciendo clic en:\n{confirm_url}\n" if confirm_url else ""
        cuerpo_texto = f"""
Tu cita ha sido registrada

¡Hola {nombre_cliente}!

Gracias por agendar una cita con nosotros. A continuación encontrarás los detalles de tu cita:

Empresa: {empresa_nombre}
Fecha: {fecha}
Hora: {hora}
Descripción: {descripcion}

{enlace_confirmacion_texto}
Si necesitas cambiar o cancelar tu cita, por favor responde a este email.

Este es un email automático.
        """

        # Adjuntar versiones del email
        mensaje.attach(MIMEText(cuerpo_texto, "plain"))
        mensaje.attach(MIMEText(cuerpo_html, "html"))

        # Conectar y enviar
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_email, smtp_password)
            server.send_message(mensaje)

        print(f"✅ Email de confirmación enviado a {destinatario}")
        return True

    except Exception as e:
        print(f"❌ Error al enviar email: {str(e)}")
        return False

