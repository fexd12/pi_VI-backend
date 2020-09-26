from app.salas import bp

from app.erros import bad_request
from app import cross_origin,db
from flask import jsonify,request
from app.authenticate import check_token_dec,decode_token
from app.models import Salas,SalasTipo
import json

@bp.route('/tipo/',methods=['GET'])
@check_token_dec
def get_sala_tipo():
    try:
        salas_tipo = SalasTipo.query.all()
        message={
            'items':[item.to_dict() for item in salas_tipo]
        }
        return jsonify(message),200
    except Exception as identifier:
        return bad_request(403,'Nao foi possivel trazer a lista de tipos de salas')

@bp.route('/',methods=['GET'])
@check_token_dec
def get_usuario():
    try:
        sala = Salas.query.all()

        users = Salas.query.join(SalasTipo,Salas.sala_tipo_id == SalasTipo.sala_tipo_id)\
        .add_columns(Salas.id_sala,Salas.numero,Salas.quantidade,SalasTipo.descricao)\
        .all()

        items= []

        for row in users:
            items.append({
            'id_sala':row[1],
            'numero':row[2],
            'quantidade':row[3],
            'salas_tipo':row[4]
            })
    
        message = {
            'items':items
        }
        
        return jsonify(message),200
    except Exception as identifier:
        return bad_request(403,'Nao foi possivel trazer as salas')

@bp.route('/',methods=['POST'])
@cross_origin()
@check_token_dec
def new_sala():
    try:
        data = request.get_json()
        data['quantidade'] = int(data['quantidade']) 
        sala = Salas()
        sala.from_dict(data)

        db.session.add(sala)
        db.session.commit()

        return jsonify({
            'message':'Sala adicionada com sucesso'
        }),200
    except Exception as identifier:
        print(identifier)
        return bad_request(403,'Nao foi possivel inserir sala')