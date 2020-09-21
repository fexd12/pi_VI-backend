from app.login import bp
from app import cross_origin
from flask_login import current_user,login_user
from app.models import Usuario,Cadastro
from flask import jsonify,request
from app.authenticate import generate_token,check_token

@bp.route('/',methods=['POST'])
@cross_origin()
def login():
    data = request.get_json()
    if current_user.is_authenticated:
        return jsonify({
            'message':'usuario {} já esta authenticado'.format(current_user.nome),
            'succes':1
        })
    if data['email'] and data['senha']:
        try:
            user = Usuario.query.filter_by(email=data['email']).first()
        except Exception as e:
            return jsonify({
                'message':'Não possui usuario com esse email'
            }),403
        check_senha = Cadastro(senha=user.cadastro_usuario[0].senha)
        if user is None or not check_senha.check(data['senha']):
            return jsonify({
                'message':'usuario e/ou senha errado',
                'succes':0
            })
        # login_user(user)
        # print(str(user.nome))
        token = generate_token(str(user.nome))
        return jsonify({
            'message':'usuario {} autenticado com sucesso '.format(str(user.nome)),
            'user': str(user.nome),
            'success':1,
            'token':token
        })
    return jsonify({
        'message':'não foi informado credenciais para login',
        'success':0
    })

@bp.route('/',methods=['GET'])
def check_login():
    token_header = request.headers.get('x-access-token')
    if token_header is None:
        return jsonify({
            'message':'Nao foi possivel localizar o token',
            'success':False
        })
    check = check_token(token_header)
    if not check:
        return jsonify({
            'message': 'invalid Token',
            'succes':0
        })
    return jsonify({
        'message':'Token Valido',
        'success':1
    })