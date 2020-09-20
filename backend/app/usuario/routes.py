from app.usuario import bp
from app import cross_origin,db
from flask import jsonify,request

from app.models import Usuario,Cadastro

@bp.route('/', methods=['GET'])
def index():
    # data = request.get_json()

    # cadastro = Cadastro()
    # cadastro.passwd(data['senha'])

    # user = Usuario(nome=data['usuario'],tag=data['tag'],cadastro_usuario=[cadastro])

    # db.session.add(user)
    # db.session.add(cadastro)
    # db.session.commit()

    message={
        'message':'pass'
    }
    return jsonify(message),200