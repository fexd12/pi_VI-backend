from flask import Flask,current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS,cross_origin
from config import Config
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
login = LoginManager()

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app,db)
    cors.init_app(app)
    login.init_app(app)

    from app.usuario import bp as usuario_bp
    app.register_blueprint(usuario_bp,url_prefix='/usuario')

    from app.login import bp as login_bp
    app.register_blueprint(login_bp,url_prefix='/login')

    from app.logout import bp as logout_bp
    app.register_blueprint(logout_bp,url_prefix='/logout')

    from app.register import bp as register_bp
    app.register_blueprint(register_bp,url_prefix='/register')

    return app

import app.models
