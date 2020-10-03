from redis import Redis 
from rq import Queue,Connection
from flask import current_app
from app import app
import smtplib

def send_mail(mail,msg):
    try:
        server = smtplib.SMTP(current_app.config['MAIL_SERVER'],current_app.config['MAIL_PORT'])
        server.starttls()
        server.login(current_app.config['MAIL_USERNAME'],current_app.config['MAIL_PASSWORD'])
        txt = msg.as_string()
        server.sendmail(current_app.config['MAIL_USERNAME'],mail,txt)
        server.quit()
    except Exception as identifier:
        return 


def queue(mail,msg):
    redis_url = current_app.config['REDIS_URL']
    with Connection(Redis.from_url(redis_url)):
        q = Queue()
        q.enqueue(send_mail,mail,msg)
