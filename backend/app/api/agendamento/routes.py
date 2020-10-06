from . import bp
from app import current_app,cross_origin,db
from flask import jsonify,request
from app.authenticate import check_token_dec,decode_token
from app.models import Agendamento,Salas
from app.erros import bad_request

@bp.route('/',methods=['POST'])
@cross_origin()
@check_token_dec
def set_agendamento():
    try:
        data = request.get_json()

        token = request.headers.get('x-access-token')

        verify_token = decode_token(token)
        user_id = verify_token['id_user']

        data['usuario_id'] = user_id

        print(data)

        agend = Agendamento()
        agend.from_dict(data)
        db.session.add(agend)
        db.session.commit()
        return jsonify({
            'message': 'Agendamento realizado com sucesso'
        }),200
    except Exception as e:
        print(e)
        return bad_request(403,'Erro ao inserir agendamento')