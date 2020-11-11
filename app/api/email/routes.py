from . import bp
from . import mail as m
from . import queue
from flask import jsonify,request,current_app
from app.erros import bad_request
from app import cross_origin
from app.authenticate import check_token_dec
from flask_mail import Message

@bp.route('/',methods=['POST'])
@cross_origin()
# @check_token_dec
def enviar_email():
    try:
        data = request.get_json()
        if data['cadastro'] ==1:
            subject = 'Cadastro Efetuado com sucesso'
            body = f"""Seu cadastro foi efetuado com sucesso
                login:{data['email']}
                senha:{data['senha']}

                Pedimos por gentileza para trocar sua senha no seu primeiro acesso.
                Ir na are de perfil para trocar sua senha
                link: www.uol.com.br
            """
        elif data['cadastro'] == 0:
            subject = 'Feedback aula'
            body = f"""
                Segue link do Formulario para nos contar como estava a sala apos a aula
                link: localhost:2000/salas/feedback
            """
        elif data['cadastro'] == 2:
            subject = 'Alteração de senha'
            body = f"""
                Foi solicitado uma alteração de senha,
                login:{data['email']}
                senha:{data['senha_nova']}
                Pedimos por gentileza para trocar sua senha no seu primeiro acesso.
                Ir na are de perfil para trocar sua senha
            """
        elif data['cadastro'] == 3:
            subject = 'Alteração de senha'
            body = f"""
                Sua senha foi alterada com sucesso
            """
        # d = m.Mail(data['email'],body,subject)
        # d.enviar()
        # queue.queue(d.email,d.msg)

        msg = Message(subject,sender=current_app.config['MAIL_USERNAME'],recipients=[data['email']])
        msg.body = body
        queue.thread_flask(msg)
        # queue.queue(data['email'],msg)

        return jsonify({
            'message':'adsasda'
        }),200
    except Exception as e:
        print(e)
        return bad_request(403,'nao foi possivel envia email')