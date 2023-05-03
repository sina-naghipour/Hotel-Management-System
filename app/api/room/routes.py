from flask import Blueprint
from .room import Room
rooms = Blueprint('rooms', __name__, url_prefix='/rooms')


@rooms.route('/get/<id>', methods=['GET'])
def getRoom(id):
    obj = Room()
    return 'hey'

@rooms.route('/add/<id>', methods=['GET'])
def addRoom(id):
    pass

@rooms.route('/update/<id>', methods=['PUT'])
def updateRoom(id):
    pass

@rooms.route('/delete/<id>', methods=['DELETE'])
def deleteRoom(id):
    pass


