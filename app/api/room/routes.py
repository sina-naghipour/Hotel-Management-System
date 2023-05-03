from flask import Blueprint, request
from .room import Room
import json
rooms = Blueprint('rooms', __name__, url_prefix='/rooms')


@rooms.route('/get/<id>', methods=['GET'])
def getRoom(id):
    obj = Room()
    return 'hey'

@rooms.route('/add', methods=['POST'])
def addRoom():
    room = json.dumps(request.json)
    room = json.loads(room)
    obj = Room()

    try:
        obj.cur.execute(f'INSERT INTO rooms (id, roomNumber, roomStatus,  customerID, bedCount, privateWC, AC, roomType) VALUES (\'{room["id"]}\', {room["roomNumber"]}, \'{room["roomStatus"]}\', \'{room["customerID"]}\', \'{room["bedCount"]}\', \'{room["privateWC"]}\', \'{room["AC"]}\', \'{room["roomType"]}\')')
        obj.save()
        return 'Room Added'
    except Exception as e:
        raise e

@rooms.route('/update/<id>/<key>/<value>', methods=['PUT'])
def updateRoom(id, key, value):
    obj = Room()

    try:
        if type(value) == str:
            obj.cur.execute(f'UPDATE rooms SET {key}=\'{value}\' WHERE id=\'{id}\' ')
            obj.save()
            return 'Room Updated'
        else:
            obj.cur.execute(f'UPDATE rooms SET {key}={value} WHERE id=\'{id}\' ')
            obj.save()
            return 'Room Updated'

    except Exception as e:
        raise e


@rooms.route('/delete/<id>', methods=['DELETE'])
def deleteRoom(id):
    obj = Room()
    try:
        obj.cur.execute(f'DELETE FROM rooms WHERE id=\'{id}\'')
        obj.save()
        return 'Room Deleted'
    except Exception as e:
        raise e

