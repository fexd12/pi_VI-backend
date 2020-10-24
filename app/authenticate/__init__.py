from werkzeug.security import generate_password_hash,check_password_hash
import jwt
from app import current_app
from flask import jsonify,request
from functools import wraps
from datetime import datetime
from time import time

def generate_hash(passwd):
    hash_passwd = generate_password_hash(passwd)
    return hash_passwd

def check_passwd(passwd,hash_passwd):
    check = check_password_hash(hash_passwd,passwd)
    return check

def decode_token(token):
    return jwt.decode(token,current_app.config['SECRET_KEY'],algorithms='HS256',options={'verify_exp':True,'verify_iat':True})

def generate_token(user,expiration_in = 7200):
    payload = {
        'user':user.nome,
        'id_user': user.id_usuario,
        'exp': time() + expiration_in,
        'iat': time()
    }
    token = jwt.encode(payload,current_app.config['SECRET_KEY'],algorithm='HS256').decode('utf-8')
    return token

def check_token(token):
    try:
        jwt.decode(token,current_app.config['SECRET_KEY'],algorithms='HS256',options={'verify_exp':True,'verify_iat':True})
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False
    except jwt.InvalidIssuedAtError:
        return False

def check_token_dec(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token_header = request.headers.get('x-access-token')
        if token_header is None:
            return jsonify({
                'message':'Nao foi possivel localizar o token',
                'success':False
            }),403
        # Remove the 'Basic" part from the token
        # auth_token = token_header.split(maxsplit=1)[1]
        # __url = "url_for_token_validation"
        # __payload = {'token' : auth_token}
        # Append the token to the header by using the payload
        # response = requests.get(__url, params=__payload, verify=False)
        # if response.status_code != requests.codes.ok:
        #     return make_response(
        #         jsonify("Invalid access as token invalid.")
        #     )
        check = check_token(token_header)
        if not check:
            return jsonify({
                'message': 'invalid Token',
                'succes':0
            }),403
        # return 
        #         jsonify("Invalid access as token invalid.")
            
        return f(*args, **kwargs)
    return decorated