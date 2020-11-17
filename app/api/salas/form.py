from flask_wtf import FlaskForm, CSRFProtect
from wtforms import RadioField
from wtforms.validators import DataRequired

csrf = CSRFProtect()

class FormSalas(FlaskForm):

    projetor = RadioField('Status do projetor',choices=[(0,'Bom'),(1,'Ruim'),(99,'Não Verificado')])
    # computador = RadioField('Status do computador',choices=[(0,'Bom'),(1,'Ruim')],validators=[DataRequired()])
    luzes = RadioField('Status das luzes',choices=[(0,'Bom'),(1,'Ruim'),(99,'Não Verificado')])
    ar = RadioField('Status do Ar-Condicionado',choices=[(0,'Bom'),(1,'Ruim'),(99,'Não Verificado')])
    
    def insert_data(self,sala_status):

        self.projetor.data = sala_status.projetor
        # self.computador.data = sala_status.computador
        self.luzes.data = sala_status.luzes
        self.ar.data = sala_status.ar