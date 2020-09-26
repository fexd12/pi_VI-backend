from flask import Blueprint

bp = Blueprint('salas',__name__)

from app.salas import routes