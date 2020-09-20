from app import db

class Agendamento(db.Model):
    __tablename__ = 'agendamento'
    id_agendamento = db.Column(db.Integer,primary_key = True)
    data = db.Column(db.DateTime)
    horario_inicio = db.Column(db.DateTime)
    horario_final = db.Column(db.DateTime)
    sala_id = db.Column(db.Integer, db.ForeignKey('salas.id_sala'),
        nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'),
        nullable=False)
