from flask_login import UserMixin
from app import db,login


class Usuario(UserMixin,db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer,primary_key = True)
    nome = db.Column(db.Text, nullable = False,unique=True)
    tag = db.Column(db.Text,nullable = False)
    agendamento = db.relationship('Agendamento', backref='agendamento_usuario', lazy=True)
    cadastro_usuario = db.relationship('Cadastro', backref='cadastro_usuario', lazy=True)

    def __repr__(self):
        return "<Usuario {}>".format(self.nome)
    
    def get_id(self):
        return self.id_usuario

@login.user_loader
def load_user(id):
    return Usuario.query.get(int(id))