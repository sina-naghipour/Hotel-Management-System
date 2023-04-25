class Room:
 
    currentObject = {}
    
    def __init__(self):
        pass
    
    # Useful & Common Getters
    
    def getRooms(self):
        pass

    def getRoomsByType(self):
        pass
    
    def getRoomsByStatus(self):
        pass
    
    def getRoomsByNumber(self):
        pass
    
    def getRoomsByBedCount(self):
        pass
    
    # CRUD Section : get, add, update, delete A Room
    
    def getRoomByID(self, id):
        pass
    
    def addRoom(self, object):
        pass
    
    def updateRoom(self, property, key):
        pass
    
    def deleteRoom(self, id):
        pass
    
    # Property Getters
    
    def getNumber(self, id):
        pass
    
    def getStatus(self, id):
        pass
    
    def getCustomerID(self, id):
        pass
    
    def getBedCount(self, id):
        pass
    
    def getprivateWC(self, id):
        pass
    
    def getAC(self, id):
        pass
    
    def getType(self, id):
        pass
    
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
