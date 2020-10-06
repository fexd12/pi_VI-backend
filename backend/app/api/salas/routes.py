from . import bp

from app.erros import bad_request
from app import cross_origin,db
from flask import jsonify,request,render_template
from app.authenticate import check_token_dec,decode_token
from app.models import Salas,SalasTipo
import json
from sqlalchemy import text


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
def get_salas():
    try:
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

@bp.route('/status/',methods=['POST'])
@cross_origin()
@check_token_dec
def teste():
    try:
        dados = request.get_json()
        with db.engine.connect() as conn:
            query = text("""
                select  t1.id_sala,
                        t1.numero,
                        t1.quantidade,
                        t1.sala_tipo_id,
                        t3.descricao as salas_tipo
                from salas t1
                join sala_tipo t3 on
	                t1.sala_tipo_id = t3.sala_tipo_id 
                where not exists (select *
                    from agendamento t2
                        where t1.id_sala = t2.sala_id and 
                        (t2.data = :data) and (t2.horario_inicio between :horario_inicio and :horario_final) and 
                        (t2.horario_final between :horario_inicio and :horario_final) ) and t1.sala_tipo_id=:sala_tipo_id
            """)
            
            result = conn.execute(query,data=dados['data'],horario_inicio = dados['horario_inicio'],horario_final=dados['horario_final'],sala_tipo_id=dados['sala_tipo_id']).fetchall()
        items = []

        for row in list(result):
            items.append({
                'id_sala': row[0],
                'numero' : row[1],
                'quantidade' :row[2],
                'sala_tipo_id' : row[3],
                'salas_tipo':row[4]
            })

        message = {
            'items': items
        }
        print(message)
        return jsonify(message),200

    except Exception as e:
        print(e)
        return bad_request(403,'não foi possivel realizar a consulta')