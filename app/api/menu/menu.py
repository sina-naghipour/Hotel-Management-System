import json
import sys,os

class Menu:

    def __init__(self):
        self.load()
        self.loadPermission()
    
    def getMenus(self):
        return self.menu
    
   
    def getMenuByID(self, id):
        for item in self.menu:
            if item['id'] == id:
                return item


    def getSubmenu(self, id):
        for item in self.menu:
            if item['id'] == id:
                return item['subMenuList']


    def load(self):
        with open('./api/menu/menu.json', 'r+') as f:            
            data = json.load(f)
            self.menu = data
            return
    
    
    def addMenu(self, json):
        self.menu.append(json)
        return
        
        
    def write(self, json):
        pass
    
    
    def loadPermission(self):
        with open('./api/menu/permission.json', 'r+') as f:            
            data = json.load(f)
            self.permission = data
            return
  
    def getPermission(self):
        return self.permission

    
    def writePermission(self, json):
        pass
    

