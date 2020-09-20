from app.logout import bp
from flask_login import logout_user
from flask import jsonify

@bp.route('/',methods=['GET'])
def logout():
    logout_user()
    return jsonify({
        'message': 'usuario deslogado com sucesso',
        'sucess': 1,
        'logout' :1
    })