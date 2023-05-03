from flask import Blueprint


menu = Blueprint('menu', __name__, url_prefix='/menu')

@menu.route('/get/<id>', moethods=['GET'])
def get(id):
    pass

@menu.route('/add', moethods=['POST'])
def add():
    pass

@menu.route('/update/<id>', moethods=['PUSH'])
def update(id):
    pass

@menu.route('/delete/<id>', moethods=['DELETE'])
def delete(id):
    pass

