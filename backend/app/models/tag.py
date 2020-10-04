from app import db

class Tag(db.Model):
    __tablename__  = 'tag'
    id_tag = db.Column(db.Integer,primary_key=True)
    tag = db.Column(db.Text,unique=True)
    ativo = db.Column(db.Text)
    
    def __repr__(self):
        return '<Tag {}>'.format(self.tag)
    
    def to_dict(self):
        data = {
            'id_tag':self.id_tag,
            'tag':self.tag
        }
        return data
    
    def from_dict(self,data):
        for field in ['id_tag','tag','ativo']:
            if field in data:
                setattr(self,field,data[field])