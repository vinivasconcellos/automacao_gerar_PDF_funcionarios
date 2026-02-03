import smtplib
from email.message import EmailMessage

#send the zip by email

def enviar_email(destinatario, assunto, corpo, anexo_path):
    msg = EmailMessage()
    msg["From"] = "vasconcellos.vinicius@hotmail.com"
    msg["To"] = destinatario
    msg["Subject"] = assunto
    msg.set_content(corpo)

    with open(anexo_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="zip",
            filename="relatorios.zip"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("vasconcellos.vinicius@hotmail.com", "SENHA_APP")
        smtp.send_message(msg)
