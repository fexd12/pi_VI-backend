from sqlalchemy.inspection import _self_inspects
from app import db

class SalasStatus(db.Model):
    __tablename__ = 'sala_status'
    sala_status_id = db.Column(db.Integer,primary_key=True)
    sala_id = db.Column(db.Integer, db.ForeignKey('salas.id_sala'),
    nullable=False,unique=True)
    projetor = db.Column(db.Text)
    luzes = db.Column(db.Text)
    ar = db.Column(db.Text)
    limpeza  = db.Column(db.Text)

    def __repr__(self):
        return "<SalasStatus {}>".format(self.sala_status_id)
    
    def to_dict(self):
        data = {
            'sala_status_id':self.sala_status_id,
            'sala_id':self.sala_id,
            'projetor':self.projetor,
            'luzes':self.luzes,
            'ar':self.ar,
            'limpeza': self.limpeza
        }
        return data
    
    def from_dict(self,data):
        for field in ['sala_id','projetor','luzes','ar','limpeza']:
            if field in data:
                setattr(self,field,data[field])