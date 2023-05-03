# Build The DataBase If It Doesn't Exist


import sqlite3

con = sqlite3.connect('hms.db')

cur = con.cursor()

# Create users table if it doesn't exist

res = cur.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'users\';')

if (res.fetchone() == None):
    cur.execute('CREATE TABLE users ( id varchar(255), roleID varchar(255), name varchar(255), username varchar(255), password varchar(255) );')
    cur.commit()
    print('CREATED users TABLE')
else : 
    print('users TABLE IS ALREADY MADE')
# Create rooms table if it doesn't exist

res = cur.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'rooms\';')

if (res.fetchone() == None):
    cur.execute('CREATE TABLE rooms ( id varchar(255), roomNumber int(255), roomStatus int(255), customerid varchar(255), bedCount int(255), privateWC int(255), AC int(255), roomType int(255) );')
    cur.commit()
    print('CREATED rooms TABLE')
else : 
    print('rooms TABLE IS ALREADY MADE')

