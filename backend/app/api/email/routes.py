from . import bp
from . import mail as m
from . import queue as q
from flask import jsonify,request
from app import cross_origin

@bp.route('/',methods=['POST'])
@cross_origin()
def enviar_email():
    data = request.get_json()
    if data['cadastro']:
        subject = 'Cadastro Efetuado com sucesso'
        body = f"""Seu cadastro foi efetuado com sucesso
            login:{data['email']}
            senha:{data['senha']}

            Pedimos por gentileza para trocar sua senha no seu primeiro acesso.
            Ir na are de perfil para trocar sua senha
            link: www.uol.com.br
        """
    else:
        subject = 'Feedback aula'
        body = """
            Segue link do Formulario para nos contar como estava a sala apos a aula
            link: www.uol.com.br
        """
    d = m.Mail(data['email'],body,subject)
    d.enviar()
    q.send_mail(d.email,d.msg)
    return jsonify({
        'message':'adsasda'
    }),200