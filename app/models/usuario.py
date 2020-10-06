from app import db
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.Text, nullable = False, unique=True)
    email = db.Column(db.Text, nullable = False, unique=True)
    ativo =  db.Column(db.Text)

    funcao_id = db.Column(db.Integer, db.ForeignKey('funcao.id_funcao'))
    acesso_id = db.Column(db.Integer, db.ForeignKey('acesso.id_acesso'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id_tag'),unique=True)

    agendamento_usuario = db.relationship('Agendamento', backref='agendamento_usuario', lazy=True)
    cadastro_usuario = db.relationship('Cadastro', backref='cadastro_usuario', lazy=True)

    def __repr__(self):
        return "<Usuario {}>".format(self.nome)
    
    def to_dict(self):
        data = {
            'id_usuario':self.id_usuario,
            'nome':self.nome,
            'email':self.email,
            'ativo':self.ativo,
            'acesso_id':self.acesso_id,
            'funcao_id':self.funcao_id,
            'tag_id':self.tag_id,
        }
        return data
    
    def from_dict(self,data,new_user=False):
        for field in ['nome','email','acesso_id','funcao_id','ativo','tag_id']:
            if field in data:
                setattr(self,field,data[field])