from datetime import date
from re import T
from app.models.usuario import Usuario
from . import bp
from app.authenticate import check_token_dec
from app import cross_origin,db
from app.models import Tag,Agendamento
from flask import jsonify,request
from app.erros import bad_request
import datetime

@bp.route('/',methods=['GET'])
@check_token_dec
def get_tag():
    tag = Tag.query.filter_by(ativo= 'S').all()

    message ={
        'items': [item.to_dict() for item in tag]
    }

    return jsonify(message),200

@bp.route('/',methods=['POST'])
@cross_origin()
def new_tag():

    data = request.get_json()
    data['ativo'] = 'S'

    try:
        tag = Tag()
        tag.from_dict(data)
    
        db.session.add(tag)
        db.session.commit()

        message = {
            'message':'Tag criada'
        }
        return jsonify(message),200

    except Exception as identifier:
        return bad_request(403,'Tag já existe')

@bp.route('/agendamento/<string:tag>/',methods=['GET'])
def agendamento(tag):

    data = datetime.datetime.today()
    hora  = str(data.hour) + ':' + str(data.minute) + ':' + '00'

    data_atual = str(data.year) + '-' + str(data.month) + '-' + str(data.day)

    agendamento = Agendamento.query.join(Usuario,Usuario.id_usuario == Agendamento.usuario_id) \
        .join(Tag,Tag.id_tag == Usuario.tag_id)\
        .add_columns(Agendamento.horario_inicio,Agendamento.horario_final)\
        .filter(Tag.tag == tag,Agendamento.data == data_atual)\
        .all()
    
    items = []

    for row in agendamento:
        horas_resultado = datetime.datetime.combine(datetime.date.today(),row[1]) - datetime.timedelta(minutes=15)
        if hora == horas_resultado.time():

            items.append({
                'horario_inicio': str(horas_resultado),
                'horario_final': str(row[2]),
            })

    print(items)
    message = {
        'items': items
    }

    return jsonify(message),200