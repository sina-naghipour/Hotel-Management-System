import sqlite3
import sys, os
import json

# {
#     "id" : "94418fe2-5d17-4bd7-a6fe-a219b78d00c9",
#     "roomNumber" : 101,
#     "roomStatus" : "FREE",
#     "customerID" : "21dfb887-b13f-4436-9195-2a59590a7619",
#     "bedCount" : 1,
#     "privateWC" : 0,
#     "AC" : 0,
#     "roomType" : 2
# }

class Room:
 
    currentObject = {}
    
    def __init__(self):
        self.db = sqlite3.connect('../hms.db')
        self.cur = self.db.cursor()
        
    
    # Useful & Common Getters
    
    def getRooms(self):
        rooms = self.cur.execute(f'SELECT * FROM rooms').fetchall()
        return rooms


    def getRoomsByType(self, type):
        rooms = self.cur.execute(f'SELECT * FROM rooms WHERE roomType = \'{type}\'').fetchall()
        return rooms

    def getRoomsByCustomerID(self, id):
        rooms = self.cur.execute(f'SELECT * FROM rooms WHERE customerID = \'{id}\'').fetchall()
        return rooms

    
    def getRoomsByStatus(self, status):
        rooms = self.cur.execute(f'SELECT * FROM rooms WHERE roomStatus = \'{status}\'').fetchall()
        return rooms

    
    def getRoomsByNumber(self, number):
        rooms = self.cur.execute(f'SELECT * FROM rooms WHERE roomNumber = \'{number}\'').fetchall()
        return rooms


    
    def getRoomsByBedCount(self, count):
        rooms = self.cur.execute(f'SELECT * FROM rooms WHERE bedCount = \'{count}\'').fetchall()
        return rooms


    
    # CRUD Section : get, add, update, delete A Room
    
    def getRoomByID(self, id):
        room = self.cur.execute(f'SELECT * FROM rooms WHERE id = \'{id}\'').fetchone()
        return room

    
    def updateRoom(self,id, property, key):
        try:
            self.cur.execute(f'UPDATE rooms SET {property} = \'{key}\' WHERE id=\'{id}\'')
        except Exception as e:
            raise e
        return 'Update Completed'


    def deleteRoom(self, id):
        try:
            self.cur.execute(f'DELETE FROM rooms WHERE id=\'{id}\'')
        except Exception as e:
            raise e
        return 'Delete Completed'
        
    
    # Property Getters
    
    def getNumber(self, id):
        room = self.cur.execute(f'SELECT * FROM rooms WHERE id = \'{id}\'').fetchone()
        return room[1]


    
    def getStatus(self, id):
        room = self.cur.execute(f'SELECT * FROM rooms WHERE id = \'{id}\'').fetchone()
        return room[2]

    
    def getCustomerID(self, id):
        room = self.cur.execute(f'SELECT * FROM rooms WHERE id = \'{id}\'').fetchone()
        return room[3]

    
    def getBedCount(self, id):
        room = self.cur.execute(f'SELECT * FROM rooms WHERE id = \'{id}\'').fetchone()
        return room[4]

    
    def getprivateWC(self, id):
        room = self.cur.execute(f'SELECT * FROM rooms WHERE id = \'{id}\'').fetchone()
        return room[5]

    
    def getAC(self, id):
        room = self.cur.execute(f'SELECT * FROM rooms WHERE id = \'{id}\'').fetchone()
        return room[6]

    
    def getType(self, id):
        room = self.cur.execute(f'SELECT * FROM rooms WHERE id = \'{id}\'').fetchone()
        return room[7]

    # Make A Room :
    # this section works with the class variable current object
    # the primary porpuse of this is to ease the workflow of scaling the project
    
    def toJson(self):
        pass
    
    def save(self):
        try:
            self.db.commit()
        except Exception as e:
            raise e
        return 'SUCCESS'
    
    def delete(self):
        pass
