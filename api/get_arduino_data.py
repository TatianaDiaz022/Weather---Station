'''
Script description:
Get temperature and humidity fron DHT11 since Arduino
Date: 07_10_2024
Developer: Tatiana Diaz
'''

#Import libraries 
import serial
import time

#Arduino port
arduino_port ='COM6'
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
        #temperature, humidity =data.split(",")
        
        #print(f"Temperature:{temperature}°C")
        #print(f"humidity:{humidity}%")    
    time.sleep(1)
    
    