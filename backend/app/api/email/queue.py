from redis import Redis 
from rq import Queue,Connection
from flask import current_app
from app import app,mail
import smtplib
from threading import Thread
from flask_mail import Message

def send_mail(mail,msg):
    try:
        server = smtplib.SMTP(current_app.config['MAIL_SERVER'],current_app.config['MAIL_PORT'])
        server.starttls()
        server.login(current_app.config['MAIL_USERNAME'],current_app.config['MAIL_PASSWORD'])
        txt = msg.as_string()
        server.sendmail(current_app.config['MAIL_USERNAME'],mail,txt)
        server.quit()
    except Exception as e:
        print(e)

def thread_mail(mail,msg):
    Thread(target=send_mail,args= (mail,msg)).start()

def queue(mail,msg):
    try:
        current_app.task_queue.enqueue(send_mail,mail,msg)
    except Exception as e:
        print(e)

def send_mail_flask(msg):
    mail.send(msg)