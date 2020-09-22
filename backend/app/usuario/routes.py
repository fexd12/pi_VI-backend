from app.usuario import bp
from app.erros import bad_request
from app import cross_origin,db
from flask import jsonify,request
from app.authenticate import check_token_dec,decode_token
from app.models import Usuario,Cadastro,Funcao,Acesso
import json

@bp.route('/', methods=['GET'])
@check_token_dec
def get_usuario():

    users = Usuario.query.all()

    message={
        'items':[item.to_dict() for item in users]
    }
    return jsonify(message),200

@bp.route('/token/', methods=['GET'])
@check_token_dec
def get_usuario_token():
    token = request.headers.get('x-access-token')

    verify_token = decode_token(token)
    user_id = verify_token['id_user']

    # users = Usuario.query.filter_by(id_usuario = user_id)

    users = Usuario.query.join(Funcao,Usuario.funcao_id == Funcao.id_funcao)\
        .join(Acesso,Usuario.acesso_id == Acesso.id_acesso)\
        .add_columns(Usuario.id_usuario,Usuario.nome,Usuario.tag,Funcao.descricao,Acesso.descricao,Usuario.email)\
        .filter(Usuario.id_usuario == user_id)\
        .first()
    
    response = {
        'id_usuario':users[1],
        'nome':users[2],
        'tag':users[3],
        'funcao':users[4],
        'acesso':users[5],
        'email':users[6]
    }

    return response,200

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

@bp.route('/reset_password/',methods=['POST'])
@cross_origin()
@check_token_dec
def reset_pass():
    token = request.headers.get('x-access-token')
    data = request.get_json()

    if int(data.get('nova_senha')):
        verify_token = decode_token(token)
        user_id = verify_token['id_user']
    else:
        user_id = data['id_usuario']

    try:
        user = Usuario.query.filter_by(id_usuario=user_id).first()
    except Exception as e:
        return jsonify({
            'message':'Não possui usuario com esse email'
        }),403
    
    if int(data.get('nova_senha')):
        try:
            check_senha = Cadastro(senha=user.cadastro_usuario[0].senha)
            if user is None or not check_senha.check(data['senha']):
                return jsonify({
                    'message':'usuario e/ou senha errado',
                    'succes':0
                }),403
        except Exception as identifier:
            return jsonify({
                'message':'Senhas não coincidem'
            }),403
    
    if data.get('senha_nova') and data.get('senha_confirma'):
        if data['senha_nova'] != data['senha_confirma']:
            return jsonify({
                'message':'as senhas nao conferem'
            }),403
    
    try:
        new_cadastro = user.cadastro_usuario[0].to_dict()

        cadastro = Cadastro()
        cadastro.from_dict(new_cadastro)
        
        cadastro.passwd(data['senha_nova'])

        user.cadastro_usuario[0].senha = cadastro.senha
        db.session.commit()
    except Exception as identifier:
        return jsonify({
            'message':'Não foi possivel alterar a sennha'
        }),403

    return jsonify({
        'message':'senha alterada com sucesso'
    }),200