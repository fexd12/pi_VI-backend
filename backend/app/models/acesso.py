from app import db

class Acesso(db.Model):
    __tablename__ = 'acesso'
    id_acesso = db.Column(db.Integer,primary_key=True)
    descricao = db.Column(db.Text)
    acesso = db.relationship('Usuario', backref='acessos', lazy=True)

    def __repr__(self):
        return "<Acesso {}>".format(self.id_acesso)