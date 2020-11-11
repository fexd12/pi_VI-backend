from flask_wtf import FlaskForm, CSRFProtect
from wtforms import RadioField
from wtforms.validators import DataRequired

csrf = CSRFProtect()

class FormSalas(FlaskForm):

    projetor = RadioField('Status do projetor',choices=[(1,'Bom'),(0,'Ruim')])
    # computador = RadioField('Status do computador',choices=[('bom','Bom'),('ruim','Ruim')],validators=[DataRequired()])
    luzes = RadioField('Status das luzes',choices=[(1,'Bom'),(0,'Ruim')])
    ar = RadioField('Status do Ar-Condicionado',choices=[(1,'Bom'),(0,'Ruim')])
    
    def insert_data(self,sala_status):

        self.projetor.data = sala_status.projetor
        # self.computador.data = sala_status.computador
        self.luzes.data = sala_status.luzes
        self.ar.data = sala_status.ar