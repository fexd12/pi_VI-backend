from .form import FormSalas
from . import bp
from app.erros import bad_request
from app import cross_origin,db
from flask import jsonify,request,render_template,redirect,url_for
from app.authenticate import check_token_dec
from app.models import Salas,SalasTipo,SalasStatus,Agendamento,Usuario
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
                        (t2.horario_final between :horario_inicio and :horario_final) ) and t1.sala_tipo_id = :sala_tipo_id and not exists (
                select t1.id_sala,t1.numero,t4.projetor,t4.luzes,t4.ar,t4.limpeza
	                from sala_status t4

		            where t1.id_sala = t4.sala_id and t4.ar = '1' or t4.projetor = '1' or t4.luzes = '1' or t4.ar = '1' or t4.limpeza= '1')
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
        # print(message)
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
                select DISTINCT COUNT(a.id_agendamento) from agendamento as a
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

@bp.route('/feedback/<uuid>/',methods=['GET','POST'])
@cross_origin()
def feedback(uuid):
    form = FormSalas()
    sala_agendada = Agendamento.query.join(Usuario,Usuario.id_usuario == Agendamento.usuario_id) \
        .join(Salas,Salas.id_sala == Agendamento.sala_id) \
        .add_columns(Usuario.nome,Usuario.email,Agendamento.sala_id,Salas.numero) \
        .filter(Agendamento.uuid == str(uuid)) \
        .first()

    if form.validate_on_submit():
        sala_status = SalasStatus.query.filter_by(sala_id = sala_agendada.sala_id).first()
        form.populate_obj(sala_status)
        db.session.add(sala_status)
        db.session.commit()
        
        return redirect(url_for('.success')) # tela para informar sucesso do cadastro
        
    return render_template('formulario.html',form=form,usuarios = sala_agendada,id = uuid)

@bp.route('/success',methods=['GET'])
@cross_origin()
def success():
    return render_template('success.html') # tela para informar sucesso do cadastro

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

@bp.route('/status_manutencao',methods=['GET'])
@cross_origin()
@check_token_dec
def status_sala_manutencao():
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

        # print(message)

        return jsonify(message),200

    except Exception as e:
        print(e)
        return bad_request(403,'não foi possivel realizar a consulta')

@bp.route('/status_limpeza',methods=['GET'])
@cross_origin()
@check_token_dec
def status_sala_limpeza():
    try:
        with db.engine.connect() as conn:
            query = text("""
                select salas.id_sala as sala_id,salas.numero,sala_status.limpeza as limpa
	                from sala_status
	                join salas on
		                sala_status.sala_id = salas.id_sala
		            where sala_status.limpeza = '1'
            """)
        
            result = conn.execute(query).fetchall()

        message = {
            'salas' : [{column: value for column, value in rowproxy.items()} for rowproxy in result]
        }

        # print(message)

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

@bp.route('/sala_manutencao', methods=['PUT'])
@cross_origin()
@check_token_dec
def sala_manutencao():
    try:
        dados = request.get_json()

        sala_padrao = {
            'ar':0,
            'luzes':0,
            'projetor':0
        }
    
        status_sala = SalasStatus.query.filter_by(sala_id = dados['id_sala']).first()
        status_sala.from_dict(sala_padrao)
        
        db.session.commit()
        
        message = {
            'message' : 'Atualização feita com sucesso'
        }
        
        return jsonify(message),200

    except Exception as e:
        print(e)
        return bad_request(403,'Não foi possivel realizar a atualização')


@bp.route('/sala_limpeza', methods=['PUT'])
@cross_origin()
@check_token_dec
def sala_limpeza():
    try:
        dados = request.get_json()

        sala_padrao = {
            'limpeza':0,
        }
    
        status_sala = SalasStatus.query.filter_by(sala_id = dados['sala_id']).first()
        status_sala.from_dict(sala_padrao)
        
        db.session.commit()
        
        message = {
            'message' : 'Atualização feita com sucesso'
        }
        
        return jsonify(message),200

    except Exception as e:
        print(e)
        return bad_request(403,'Não foi possivel realizar a atualização')

@bp.route('/limpeza', methods=['GET'])
@check_token_dec
def func_limpeza():
    try:
        
        salas = SalasStatus.query.filter(SalasStatus.limpeza == '1') \
        .count()

        message = { 
            'salas': salas
        }

        return jsonify(message),200

    except Exception as e:
        print(e)
        return bad_request(403,'Não foi possivel encontrar usuário')