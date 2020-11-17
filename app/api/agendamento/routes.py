from . import bp
from app import current_app,cross_origin,db
from flask import jsonify,request
from app.authenticate import check_token_dec,decode_token
from app.models import Agendamento as A
from app.models import Salas as S
from app.models import SalasTipo as ST
from app.erros import bad_request
from datetime import date,timedelta
import uuid

dia = date.today()

@bp.route('/',methods=['GET'])
@check_token_dec
def get_agendamento():
    try:

        token = request.headers.get('x-access-token')
        verify_token = decode_token(token)
        user_id = verify_token['id_user']
        dia_futuro = dia + timedelta(days=7)
        agend = A.query.join(S,S.id_sala == A.sala_id ) \
            .join(ST,ST.sala_tipo_id == S.sala_tipo_id) \
            .add_columns(A.id_agendamento, A.data, A.horario_inicio, A.horario_final, S.id_sala, S.numero, ST.descricao) \
            .filter(A.usuario_id == user_id,A.data.between(dia,dia_futuro)) \
            .all()

        items = []

        for row in agend:
            items.append({
                'id_agendamento':row[1],
                'data': str(row[2]),
                'horario_inicio': str(row[3]),
                'horario_final': str(row[4]),
                'id_sala':row[5],
                'numero':row[6],
                'tipo_sala':row[7]
            })

        message = {
            'items': items
        }
        return jsonify(message),200

    except Exception as e:
        print(e)
        return bad_request(403,'não foi possivel carregar o agendamento')

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
        data['uuid'] = uuid.uuid4()

        agend = A()
        agend.from_dict(data)
        db.session.add(agend)
        db.session.commit()
        return jsonify({
            'message': 'Agendamento realizado com sucesso'
        }),200
    except Exception as e:
        return bad_request(403,'Erro ao inserir agendamento')

@bp.route('/',methods=['PUT'])
@cross_origin()
@check_token_dec
def delete_agendamento():

    try:
        data = request.get_json()
        delet_agendamento = A.query.filter_by(id_agendamento=data['id_agendamento']).first()
        
        db.session.delete(delet_agendamento)
        db.session.commit()
        return jsonify({
            'message': 'Agendamento '
        }),200

    except Exception as e:
        print(e)
        return bad_request(403,'erro ao deletar o agendamento')