'''
Dev: Tatian D.
Script description : Weather - Station DataBase
Engine: SQLite3
Data: 09-09-2024
'''

#Import database engine package
import sqlite3

#Create Weather-station database connection
con = sqlite3.connect('weather_station.db')

#Create cursor
#permite ejecutar las  operaciones cur
cur = con.cursor() 

#User model
users_model = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        pasword TEXT NOT NULL,
        role TEXT NOT NULL,
        status BOOLEAN DEFAUL true,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        update_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        deleted_at null
    )
'''

#Execute query
cur.execute(users_model)

#Close connection
con.close()
