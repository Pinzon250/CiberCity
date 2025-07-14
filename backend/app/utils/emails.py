import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ORIGEN = os.getenv("EMAIL_ORIGEN")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
FRONT_URL = os.getenv("FRONT_URL")

def enviar_correo_promocion(destinatario: str, producto: str, descuento: float):
    msg = EmailMessage()
    msg['Subject'] = f"¡Oromocion en {producto}!"
    msg['From'] = EMAIL_ORIGEN
    msg['To'] = destinatario

    msg.set_content(f"¡Buenas noticias!\n\nEl producto '{producto}' que tienes en tu lista de deseos ahora tiene un {descuento}% de descuento.\n\n¡Visítanos y aprovecha esta promoción!")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ORIGEN, MAIL_PASSWORD)
        smtp.send_message(msg)

def enviar_correo_verificacion(
        destinatario: str,
        token: str
):
    msg = EmailMessage()
    msg['Subject'] = "Verifica tu cuenta de Cibercity"
    msg["From"] = EMAIL_ORIGEN
    msg["To"] = destinatario

    enlace = f"{FRONT_URL}/verificar-cuenta?token={token}"
    msg.set_content(f"""¡Gracias por registrarte en Cibercity!

Verifica tu cuenta haciendo click en el siguiente enlace: 
{enlace}

Si no solicitaste esta cuenta, puedes ignorar este mensaje.
""")
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ORIGEN, MAIL_PASSWORD)
        smtp.send_message(msg)