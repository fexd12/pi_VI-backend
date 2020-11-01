from setuptools.unicode_utils import try_encode
from .form import Form
from . import bp
from app.erros import bad_request
from app import cross_origin,db
from flask import jsonify,request,render_template,redirect
from app.authenticate import check_token_dec
from app.models import Salas,SalasTipo,SalasStatus
import json
from sqlalchemy import text
from datetime import date

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
        data_sala = {
            'sala_id':sala.id_sala
        }

        sala_status =  SalasStatus()
        sala_status.from_dict(data_sala)

        db.session.add(sala_status)
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
                        (t2.data = :data) and not (t2.horario_inicio between :horario_inicio and :horario_final) and not
                        (t2.horario_final between :horario_inicio and :horario_final) ) and t1.sala_tipo_id = :sala_tipo_id
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

@bp.route('/alugada',methods=['GET'])
@check_token_dec
def sala_alugada():
    try:
        data = date.today()
        with db.engine.connect() as conn:
            query = text("""
                select DISTINCT COUNT(s.id_sala) from agendamento as a
	                join salas as s on 
		                a.sala_id = s.id_sala
	                where a.data = :data_atual
            """)
            
            result = conn.execute(query,data_atual=data).fetchall()
        
        message ={
            'salas' : result[0][0]
        }

        return jsonify(message),200

    except Exception as e:
        print(e)
        return bad_request(403,'não foi possivel realizar a consulta')

@bp.route('/feedback',methods=['GET','POST'])
@cross_origin()
def feedback():
    form = Form()
    if form.validate_on_submit():
        #enviar resposta ao banco 
        #request.form

        return render_template('success.html') # tela para informar sucesso do cadastro
        
    return render_template('formulario.html',form=form),200

# @bp.route('/teste_feedback',methods=['POST'])
# @cross_origin()
# def teste_feedback():
#     # print('teste')
#     name = request.form['projetor']
#     # luzes = request.form['luzes']
#     print(name)
#     return jsonify('teste'),200 # tela para informar sucesso do cadastro

@bp.route('/manutencao',methods=['GET'])
@cross_origin()
@check_token_dec
def salass_manutencao():
    try:
        data = date.today()
        with db.engine.connect() as conn:
            query = text("""
                select distinct count(sala_id)
	                from sala_status 
		                where ar = '1' or projetor = '1' or luzes = '1' or ar = '1'
            """)
            
            result = conn.execute(query,data_atual=data).fetchall()
        
        message ={
            'salas' : result[0][0]
        }

        return jsonify(message),200

    except Exception as e:
        print(e)
        return bad_request(403,'não foi possivel realizar a consulta')

@bp.route('/status',methods=['GET'])
@cross_origin()
def status_sala():
    try:
        with db.engine.connect() as conn:
            query = text("""
                select salas.id_sala,salas.numero,sala_status.projetor,sala_status.luzes,sala_status.ar
	                from sala_status
	                join salas on
		                sala_status.sala_id = salas.id_sala
		            where sala_status.ar = '1' or sala_status.projetor = '1' or sala_status.luzes = '1' or sala_status.ar = '1'

            """)
        
            result = conn.execute(query).fetchall()

        message ={
            'salas' : [{column: value for column, value in rowproxy.items()} for rowproxy in result]
        }

        print(message)

        return jsonify(message),200

    except Exception as e:
        print(e)
        return bad_request(403,'não foi possivel realizar a consulta')

@bp.route('/disponivel',methods=['GET'])
@cross_origin()
@check_token_dec
def sala_disponivel():
    try:
        salas = Salas.query.count()

        message ={
            'salas' : salas
        }

        return jsonify(message),200

    except Exception as e:
        print(e)
        return bad_request(403,'não foi possivel realizar a consulta')