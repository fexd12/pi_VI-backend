from app.logout import bp
from flask_login import logout_user
from flask import jsonify
from app import cross_origin

@bp.route('/',methods=['GET'])
@cross_origin()
def logout():
    logout_user()
    return jsonify({
        'message': 'usuario deslogado com sucesso',
        'sucess': 1,
        'logout' :1
    })