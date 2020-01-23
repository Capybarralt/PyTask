import hashlib

attempt = 1
login = False

def make_token(username, password):
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()

def login_required(func):
    def wrapper(*args, **kwargs):
        global attempt
        global login
        if not login:
            while attempt <= 3:
                username = input()
                password = input()
                with open('token.txt', 'r') as f:
                    token = f.read()
                if make_token(username, password) in token:
                    login = True
                    return func(*args, **kwargs)
                else:
                    attempt += 1
            else:
                raise RuntimeError('Authentication failed')
        return func(*args, **kwargs)
    return wrapper
