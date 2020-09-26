from flask import Flask,current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_cors import CORS,cross_origin

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)

    from app.usuario import bp as usuario_bp
    app.register_blueprint(usuario_bp,url_prefix='/usuario')

    from app.login import bp as login_bp
    app.register_blueprint(login_bp,url_prefix='/login')
    
    from app.salas import bp as salas_bp
    app.register_blueprint(salas_bp,url_prefix='/salas')

    return app

import app.models
