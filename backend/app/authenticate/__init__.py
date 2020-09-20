from werkzeug.security import generate_password_hash,check_password_hash

def generate_hash(passwd):
    hash_passwd = generate_password_hash(passwd)
    return hash_passwd

def check_passwd(passwd,hash_passwd):
    check = check_password_hash(hash_passwd,passwd)
    return check
