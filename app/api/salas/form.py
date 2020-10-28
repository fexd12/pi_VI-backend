from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField,RadioField

csrf = CSRFProtect()

class Form(FlaskForm):

    projetor = RadioField('Status do projetor',choices=[('bom','Bom'),('ruim','Ruim')])
    computador = RadioField('Status do computador',choices=[('bom','Bom'),('ruim','Ruim')])
    luzes = RadioField('Status das luzes',choices=[('bom','Bom'),('ruim','Ruim')])
    ar = RadioField('Status do Ar-Condicionado',choices=[('bom','Bom'),('ruim','Ruim')])

    mensagem = TextAreaField('Escreva alguma observação:')
