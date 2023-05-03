from flask import Blueprint, request, session
from cryptography.fernet import Fernet
from .user import User
import json, jwt
import uuid
import time
 

users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/auth', methods=['GET'])
def authPage():
    obj = User()
    user = obj.getUser('113ce4fc-f21b-430c-90ac-9f4277c614bd')
    return obj.toJSON(user)


@users.route('/auth', methods=['POST'])
def auth():
    user = json.dumps(request.json)
    user = json.loads(user)
    
    user['loginTime'] = str(time.asctime(time.localtime(time.time())))
    del user['password']
    
    token = jwt.encode(user, 'SECRET_KEY', algorithm='HS384')

    session[str(uuid.uuid4())] = token

    return token
    
@users.route('/logout', methods=['POST'])
def logout():
    token = request.headers.get('Authorization')
    
    for key, item in session.items():
        if item == token:
            session.pop(key, None)
            return 'Logged Out'
    return 'No Such Token Was Ever Logged In'


@users.route('/role/<id>', methods=['GET'])
def getRole(id):
    pass

@users.route('/checkAuth', methods=['POST'])
def isLoggedIn():
    pass

@users.route('/get/<id>', methods=['GET'])
def get(id):
    pass

@users.route('/add/<id>', methods=['POST'])
def add(id):
    pass

@users.route('/update/<id>', methods=['PUT'])
def update(id):
    pass

@users.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    pass




