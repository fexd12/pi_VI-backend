from flask import jsonify,request
from flask_login import current_user

from app import cross_origin,db
from app.register import bp
from app.models import Usuario,Cadastro

@bp.route('/', methods=['POST'])
def index():
    data = request.get_json()
    
    if current_user.is_authenticated:
        return jsonify({
            'message':'usuario {} já esta authenticado'.format(current_user.nome),
            'succes':1
        })

    if data['usuario'] and data['senha'] and data['tag']:
        try:
            cadastro = Cadastro()
            cadastro.passwd(data['senha'])

            user = Usuario(nome=data['usuario'],tag=data['tag'],cadastro_usuario=[cadastro])

            db.session.add(user)
            db.session.add(cadastro)
            db.session.commit()

        except Exception as e:
            return jsonify({
                'message': 'houve um problema ao registrar o usuario',
                'success':0
            })
        message={
            'message':'usuario inserido com sucesso'
        }
        return jsonify(message),200
    return jsonify({
        'message': 'não foi possivel inserir o usuario. Confira os dados enviados',
        'success': 0
    })