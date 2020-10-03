from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from flask import current_app

"""
O email deve ser enviado quando o ADMIN realizar o cadastro do USUARIO , e quando FINALIZAR o  horario do agendamento
"""

class Mail():
    def __init__(self,email,body,subject):
        self.msg = MIMEMultipart()
        self.body = body
        self.email = email
        self.subject  = subject

    def enviar(self):
        self.msg['From'] = current_app.config['MAIL_USERNAME']
        self.msg['To'] = self.email
        self.msg['Subject'] = self.subject
        mensagem = self.body
        self.msg.attach(MIMEText(mensagem,'plain'))
