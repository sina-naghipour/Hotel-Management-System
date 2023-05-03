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
    
    obj = User()
    result = obj.getUserByUsername(user['username'])
    
    if result == 'User With That username Not Found':
                
        user['loginTime'] = str(time.asctime(time.localtime(time.time())))
        del user['password']
    
        token = jwt.encode(user, 'SECRET_KEY', algorithm='HS384')

        session[str(uuid.uuid4())] = token

        return token

    return 'Wrong Credentials'


@users.route('/logout', methods=['POST'])
def logout():
    token = request.headers.get('Authorization')
    
    for key, item in session.items():
        if item == token:
            session.pop(key, None)
            return 'Logged Out'
    return 'No Such Token Was Ever Logged In'


@users.route('/checkAuth', methods=['POST'])
def isLoggedIn():
    token = request.headers.get('Authorization')
    
    for key, item in session.items():
        if item == token:
            return 'User Is Logged In'
    return 'User Is Not Logged In'


@users.route('/<id>/role', methods=['GET'])
def getRole(id):
    obj = User()
    result = obj.getRoleID(id)
    return result


@users.route('/<id>/get', methods=['GET'])
def get(id):
    obj = User()
    result = obj.getUser(id)
    result = json.dumps(result)
    return json.loads(result)



@users.route('/add', methods=['POST'])
def add(id):
    pass


@users.route('/<id>/update', methods=['PUT'])
def update(id):
    pass


@users.route('/<id>/delete', methods=['DELETE'])
def delete(id):
    pass




