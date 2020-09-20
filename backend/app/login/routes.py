from app.login import bp
from app import cross_origin
from flask_login import current_user,login_user
from app.models import Usuario,Cadastro
from flask import jsonify,request

@bp.route('/',methods=['POST'])
def login():
    data = request.get_json()
    if current_user.is_authenticated:
        return jsonify({
            'message':'usuario {} já esta authenticado'.format(current_user.nome),
            'succes':1
        })
    if data['usuario'] and data['senha']:
        user = Usuario.query.filter_by(nome=data['usuario']).first()
        check_senha = Cadastro(senha=user.cadastro_usuario[0].senha)
        print(user.id_usuario)
        if user is None or not check_senha.check(data['senha']):
            return jsonify({
                'message':'usuario e/ou senha errado',
                'succes':0
            })
        login_user(user)
        return jsonify({
            'message':'usuario {} autenticado com sucesso '.format(current_user.nome),
            'succes':1
        })
    return jsonify({
        'message':'não foi informado credenciais para login',
        'success':0
    })
