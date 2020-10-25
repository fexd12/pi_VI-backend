from . import bp
from app.authenticate import check_token_dec
from app import cross_origin,db
from app.models import Tag
from flask import jsonify,request
from app.erros import bad_request

@bp.route('/',methods=['GET'])
@check_token_dec
def get_tag():
    tag = Tag.query.filter_by(ativo= 'S').all()

    message ={
        'items': [item.to_dict() for item in tag]
    }

    return jsonify(message),200

@bp.route('/',methods=['POST'])
@cross_origin()
def new_tag():

    data = request.get_json()
    data['ativo'] = 'S'

    try:
        tag = Tag()
        tag.from_dict(data)
    
        db.session.add(tag)
        db.session.commit()

        message = {
            'message':'Tag criada'
        }
        return jsonify(message),200

    except Exception as identifier:
        return bad_request(403,'Tag já existe')

    