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
        password TEXT NOT NULL,
        role INTEGER NOT NULL DEFAULT 1,
        status BOOLEAN DEFAULT true,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        update_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        deleted_at null
    )
'''
#Sensor model
sensors_model = '''
    CREATE TABLE IF NOT EXISTS sensors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        model TEXT NOT NULL,
        description TEXT NOT NULL,
        url_datasheet TEXT NULL,
        url_image TEXT NULL,
        status BOOLEAN DEFAULT true,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        deleted_at NULL
        )
'''

#Execute query
cur.execute(users_model)
cur.execute(sensors_model)

#Close connection
#con.close()
