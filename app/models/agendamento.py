from app import db

class Agendamento(db.Model):
    __tablename__ = 'agendamento'
    id_agendamento = db.Column(db.Integer,primary_key = True)
    data = db.Column(db.Date)
    horario_inicio = db.Column(db.Time)
    horario_final = db.Column(db.Time)
    uuid = db.Column(db.Text)

    sala_id = db.Column(db.Integer, db.ForeignKey('salas.id_sala'),
        nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'),
        nullable=False)

    def to_dict(self):
        data = {
            'id_agendamento' :self.id_agendamento,
            'data':str(self.data),
            'horario_inicio':str(self.horario_inicio),
            'horario_final': str(self.horario_final),
            'sala_id': self.sala_id,
            'usuario_id': self.usuario_id,
            'uuid':self.uuid
        }
        return data

    def from_dict(self,data):
        for field in ['data','horario_inicio','horario_final','sala_id','usuario_id','uuid']:
            if field in data:
                setattr(self,field,data[field])
        
