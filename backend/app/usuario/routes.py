from app.usuario import bp
from app.erros import bad_request
from app import cross_origin,db
from flask import jsonify,request
from app.authenticate import check_token_dec
from app.models import Usuario,Cadastro

@bp.route('/', methods=['GET'])
@check_token_dec
def get_usuario():

    users = Usuario.query.all()

    message={
        'items':[item.to_dict() for item in users]
    }
    return jsonify(message),200

@bp.route('/',methods=['POST'])
@cross_origin()
@check_token_dec
def new_user():
    data = request.get_json()

    if 'nome' not in data or 'email' not in data or 'senha' not in data or 'tag' not in data:
        return bad_request('Precisa passar nome, email,senha e tag')
    if Usuario.query.filter_by(nome=data['nome']).first():
        return bad_request('Use um outro nome')
    if Usuario.query.filter_by(email=data['email']).first():
        return bad_request('Use um outro email')
    
    usuario = Usuario()
    usuario.from_dict(data)

    cadastro = Cadastro()
    cadastro.passwd(data['senha'])

    usuario.cadastro_usuario = [cadastro]

    db.session.add(usuario)
    db.session.add(cadastro)
    db.session.commit()

    message = {
        'message':'usuario criado'
    }

    return jsonify(message),200