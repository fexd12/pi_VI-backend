from app import db

class Salas(db.Model):
    __tablename__ = 'salas'
    id_sala = db.Column(db.Integer,primary_key = True)
    numero = db.Column(db.Text,unique=True)
    tipo = db.Column(db.Text)
    quantidade = db.Column(db.Integer)
    agendamento = db.relationship('Agendamento', backref='salas', lazy=True)
    
    def __repr__(self):
        return "<Sala {}>".format(self.numero)