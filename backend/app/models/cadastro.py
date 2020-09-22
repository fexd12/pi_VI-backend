from app import db
from app.authenticate import generate_hash,check_passwd

class Cadastro(db.Model):
    __tablename__ = 'cadastro_usuario'
    id_cadastro = db.Column(db.Integer,primary_key = True)
    senha = db.Column(db.Text, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'),
    nullable=False,unique=True)

    def __repr__(self):
        return "<Cadastro {}>".format(self.usuario_id)

    def passwd(self,passwd):
        self.senha = generate_hash(passwd)
    
    def check(self,passwd):
        return check_passwd(passwd,self.senha)

    def to_dict(self):
        data = {
            'id_cadastro':self.id_cadastro,
            'usuario_id':self.usuario_id,
            'senha':self.senha
        }
        return data

    def from_dict(self,data):
        for field in ['id_cadastro','usuario_id','senha']:
            if field in data:
                setattr(self,field,data[field])