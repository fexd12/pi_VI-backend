from app import db

class Salas(db.Model):
    __tablename__ = 'salas'
    id_sala = db.Column(db.Integer,primary_key = True)
    numero = db.Column(db.Text,unique=True)
    quantidade = db.Column(db.Integer)
    
    sala_tipo_id = db.Column(db.Integer, db.ForeignKey('sala_tipo.sala_tipo_id'))

    sala_status = db.relationship('SalasStatus', backref='sala_status', lazy=True)

    agendamento_sala = db.relationship('Agendamento', backref='agendamento_sala', lazy=True)
    
    def __repr__(self):
        return "<Sala {}>".format(self.numero)
    
    def from_dict(self,data):
        for field in ['numero','quantidade','sala_tipo_id']:
            if field in data:
                setattr(self,field,data[field])

    def to_dict(self):
        data = {
            'id_sala': self.id_sala,
            'numero': self.numero,
            'quantidade': self.quantidade
        }
        return data