import sqlite3
import sys, os
import json
class User:

    '''
        This class handles interaction with users table, these action
        include listing users by specific conditons (such as roles),
        getting specific properties and setting them.    
    '''

    def __init__(self, id=None):

        self.db = sqlite3.connect('../hms.db')
        print(os.getcwd())
        self.cur = self.db.cursor()
        if id != None :
            self.currentUser = self.cur.execute(f'SELECT * FROM users WHERE id=\'{id}\'').fetchone()
        
    # Useful & Common Getters
    
    def getUser(self, id):
        user = self.cur.execute(f'SELECT * FROM users WHERE id=\'{id}\'').fetchone()
        if user == None:
            return 'User With That ID Not Found'
        else:
            return user

    def getUsersByRole(self, roleID):
        users = self.cur.execute(f'SELECT * FROM users WHERE roleID=\'{roleID}\'').fetchall()
        if users == None:
            return 'No User Has That Specific Role'
        else:
            return users

    def getUserByName(self, name):
        user = self.cur.execute(f'SELECT * FROM users WHERE name=\'{name}\'').fetchone()
        if user == None:
            return 'User With That Name Not Found'
        else:
            return user


    def getUserByUsername(self, username):
        user = self.cur.execute(f'SELECT * FROM users WHERE username=\'{username}\'').fetchone()
        if user == None:
            return 'User With That username Not Found'
        else:
            return user


    # get user information
    
    def getPassword(self, id):
        user = self.cur.execute(f'SELECT * FROM users WHERE id=\'{id}\'').fetchone()
        if user == None:
            return 'User With That id Not Found'
        else:
            return user[4]

    def getUsername(self, id):
        user = self.cur.execute(f'SELECT * FROM users WHERE id=\'{id}\'').fetchone()
        if user == None:
            return 'User With That id Not Found'
        else:
            return user[3]
    
    
        
    def getName(self, id):
        user = self.cur.execute(f'SELECT * FROM users WHERE id=\'{id}\'').fetchone()
        if user == None:
            return 'User With That id Not Found'
        else:
            return user[2]
    
    def getRoleID(self, id):
        user = self.cur.execute(f'SELECT * FROM users WHERE id=\'{id}\'').fetchone()
        if user == None:
            return 'User With That id Not Found'
        else:
            return user[1]
    
    
    # set user information
    
    def setRoleID(self, id, value):
        user = self.cur.execute(f'UPDATE users SET roleID=\'{value}\' WHERE id=\'{id}\'').fetchone()
        if user == None:
            return 'User With That id Not Found'
        else:
            return f'RoleID of The User : {id} Has Been Changed'
    
    def setName(self, id, value):
        user = self.cur.execute(f'UPDATE users SET name=\'{value}\' WHERE id=\'{id}\'').fetchone()
        if user == None:
            return 'User With That id Not Found'
        else:
            return f'Name of The User : {id} Has Been Changed'
    
    def setUsername(self, id, value):
        user = self.cur.execute(f'UPDATE users SET username=\'{value}\' WHERE id=\'{id}\'').fetchone()
        if user == None:
            return 'User With That id Not Found'
        else:
            return f'Username of The User : {id} Has Been Changed'

    
    def setPassword(self, id, value):
        user = self.cur.execute(f'UPDATE users SET password=\'{value}\' WHERE id=\'{id}\'').fetchone()
        if user == None:
            return 'User With That id Not Found'
        else:
            return f'Password of The User : {id} Has Been Changed'

    
    # Misc. Functions
    
    def toJSON(self, user):
        result = {}
        result['id'] = user[0]
        result['roleID'] = user[1]
        result['name'] = user[2]
        result['username'] = user[3]
        
        return json.dumps(result)
    