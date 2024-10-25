'''
Script description:
Get temperature and humidity fron DHT11 since Arduino
Date: 07_10_2024
Developer: Tatiana Diaz
'''

#Import libraries 
import serial
import serial.tools.list_ports
import time
import detect_arduino_port import p

#Arduino port
arduino_port = p
arduino_bau = 9600

service = serial.Serial(
    arduino_port,
    arduino_bau,
    timeout = 1
)

time.sleep(1) #delaty

while True:
    #data = service.readline.decode('utf-8').strip()
    data = service.readline().decode('utf-8').rstrip() 
    
    if data:
        print(data)
        temperature, humidity = data.split(",")
        print(f"Temperature:{temperature}°C")
        print(f"humidity:{humidity}%")    
        
        #1. create a new model data called "test_data"
        #Fidelds: id, temp, hum, created_at
        #2. create method to insert data into test_data 
        #3. update method. instert data whe detec chages in temp or hum 
        
    time.sleep(1)
    
    