#com Outlook COM, local e funciona bem pra automação. Ainda teria uma com Cloud para produção que é melhor ainda
# import logging
# import win32com.client as win32
# import os

# def enviar_email(destinatario, assunto, corpo, anexo_path):
#     try:
#         logging.info("Iniciando envio de email via Outlook")
        
#         if not os.path.exists(anexo_path):
#             raise FileNotFoundError(f"Anexo não encontrado: {anexo_path}")

#         outlook = win32.Dispatch("Outlook.Application")
#         mail = outlook.CreateItem(0)

#         mail.To = destinatario
#         mail.Subject = assunto
#         mail.Body = corpo
#         mail.Attachments.Add(os.path.abspath(anexo_path))

#         mail.Send()

#         logging.info("Email enviado com sucesso via Outlook")

#     except Exception:
#         logging.error("Erro ao enviar email via Outlook", exc_info=True)
#         raise


# #SMTP but unusual, because block security, expo credentials, not really used on the market  
# import smtplib
# import logging
# from email.message import EmailMessage

# def enviar_email(destinatario, assunto, corpo, anexo_path):
#     try:
#         logging.info("Iniciando envio de email")

#         msg = EmailMessage()
#         msg["From"] = "vasconcellos.vinicius@hotmail.com"
#         msg["To"] = destinatario
#         msg["Subject"] = assunto
#         msg.set_content(corpo)

        # with open(anexo_path, "rb") as f:
        #     msg.add_attachment(
        #         f.read(),
        #         maintype="application",
        #         subtype="zip",
        #         filename="relatorios.zip"
        #     )

#         with smtplib.SMTP_SSL("smtp.office365.com", 587) as smtp:
#             smtp.login("vasconcellos.vinicius@hotmail.com", "SENHA_APP")
#             smtp.send_message(msg)

#         logging.info("Email enviado com sucesso")

#     except Exception as e:
#         logging.error("Erro ao enviar email", exc_info=True)
#         raise


