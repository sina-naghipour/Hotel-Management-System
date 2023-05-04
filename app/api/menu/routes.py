from flask import Blueprint, request
from .menu import Menu
import json

menu = Blueprint('menu', __name__, url_prefix='/menu')

@menu.route('/get/<id>', methods=['GET'])
def get(id):
    obj = Menu()
    li = []
    for item in obj.permission:
        if item['id'] == id:
            for i in item['permission']:
                li.append(obj.getMenuByID(i))

    return li


@menu.route('/add', methods=['POST'])
def add():
    temp = json.dumps(request.json)
    temp = json.loads(temp)
    obj = Menu()
    try:
        obj.addMenu(temp)
        print(obj.getMenus())
        return 'hey'
    except Exception as e:
        raise e
        
    
@menu.route('/update/<id>', methods=['PUSH'])
def update(id):
    pass


@menu.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    pass

