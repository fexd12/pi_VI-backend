from app import db
class Funcao(db.Model):
    __tablename__ = 'funcao'
    id_funcao = db.Column(db.Integer,primary_key=True)
    descricao = db.Column(db.Text)
    funcao = db.relationship('Usuario', backref='funcoes', lazy=True)

    def __repr__(self):
        return "<Funcao {}>".format(self.id_funcao)

    def to_dict(self):
        data = {
            'id_funcao':self.id_usuario,
            'descricao':self.nome,
            'funcao':self.funcao
        }
        return data