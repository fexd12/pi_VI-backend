from app import db

class SalasTipo(db.Model):
    __tablename__ = 'sala_tipo'
    sala_tipo_id = db.Column(db.Integer,primary_key=True)
    descricao = db.Column(db.Text)

    sala_tipo = db.relationship('Salas', backref='sala_tipo', lazy=True)

    def __repr__(self):
        return "<SalasTipo {}>".format(self.sala_tipo_id)
    
    def to_dict(self):
        data = {
            'sala_tipo_id':self.sala_tipo_id,
            'descricao':self.descricao
        }
        return data