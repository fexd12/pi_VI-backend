from flask_login import UserMixin
from app import db,login


class Usuario(UserMixin,db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.Text, nullable = False, unique=True)
    email = db.Column(db.Text, nullable = False, unique=True)
    tag = db.Column(db.Text, nullable = False)

    funcao_id = db.Column(db.Integer, db.ForeignKey('funcao.id_funcao'))
    acesso_id = db.Column(db.Integer, db.ForeignKey('acesso.id_acesso'))

    agendamento = db.relationship('Agendamento', backref='agendamento_usuario', lazy=True)
    cadastro_usuario = db.relationship('Cadastro', backref='cadastro_usuario', lazy=True)

    def __repr__(self):
        return "<Usuario {}>".format(self.nome)
    
    def get_id(self):
        return self.id_usuario
    
    def to_dict(self):
        data = {
            'id_usuario':self.id_usuario,
            'nome':self.nome,
            'email':self.email,
            'tag':self.tag,
            'acesso_id':self.acesso_id,
            'funcao_id':self.funcao_id
        }
        return data
    
    def from_dict(self,data,new_user=False):
        for field in ['nome','email','tag','acesso_id','funcao_id']:
            if field in data:
                setattr(self,field,data[field])


@login.user_loader
def load_user(id):
    return Usuario.query.get(int(id))