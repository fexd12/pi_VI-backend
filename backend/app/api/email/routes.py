from . import bp
from . import mail as m
from . import queue as q
from flask import jsonify
from app import cross_origin

@bp.route('/',methods=['POST'])
@cross_origin()
def enviar_email():
    d = m.Mail('email','teste','teste-2')
    d.enviar()
    q.send_mail(d.email,d.msg)
    return jsonify({
        'message':'adsasda'
    }),200