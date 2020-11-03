from app.api.salas.routes import teste
from flask import current_app
from app import mail
import smtplib
from threading import Thread

def send_mail(mail,msg):
    try:
        # print('email')
        server = smtplib.SMTP(current_app.config['MAIL_SERVER'],current_app.config['MAIL_PORT'])
        server.starttls()
        server.login(current_app.config['MAIL_USERNAME'],current_app.config['MAIL_PASSWORD'])
        txt = msg.as_string()
        server.sendmail(current_app.config['MAIL_USERNAME'],mail,txt)
        server.quit()
    except Exception as e:
        raise e

def thread_mail(mail,msg):
    Thread(target=send_mail,args= (mail,msg)).start()

def queue(mail,msg):
    try:
        current_app.task_queue.enqueue(send_mail,mail,msg)
    except Exception as e:
        raise e 

def send_mail_flask(app,msg):
    with app.app_context():
        mail.send(msg)

def thread_flask(msg):
    
    Thread(target=send_mail_flask,args= (current_app._get_current_object(),msg)).start()