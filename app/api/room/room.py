import sqlite3
import sys, os
import json

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
        rooms = self.cur.execute(f'SELECT * FROM rooms WHERE id = \'{id}\'').fetchall()
        return rooms


    
    def addRoom(self, object):
        pass
    
    def updateRoom(self, property, key):
        pass
    
    def deleteRoom(self, id):
        pass
    
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

    
    # Property Setters
    
    def setNumber(self, id):
        pass
    
    def setStatus(self, id):
        pass
    
    def setCustomerID(self, id):
        pass
    
    def setBedCount(self, id):
        pass
    
    def setPrivateWC(self, id):
        pass
    
    def setAC(self, id):
        pass
    
    def setType(self, id):
        pass
    
    # Make A Room :
    # this section works with the class variable current object
    # the primary porpuse of this is to ease the workflow of scaling the project
    
    def toJson(self):
        pass
    
    def save(self):
        pass
    
    def delete(self):
        pass
