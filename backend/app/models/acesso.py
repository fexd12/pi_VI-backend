from app import db
from sqlalchemy_serializer import SerializerMixin

class Acesso(db.Model, SerializerMixin):
    __tablename__ = 'acesso'
    id_acesso = db.Column(db.Integer,primary_key=True)
    descricao = db.Column(db.Text)
    acesso = db.relationship('Usuario', backref='acessos', lazy=True)

    def __repr__(self):
        return "<Acesso {}>".format(self.id_acesso)
    
    def to_dict(self):
        data = {
            'id_acesso':self.id_acesso,
            'descricao':self.descricao,
            'acesso':self.acesso
        }
        return data