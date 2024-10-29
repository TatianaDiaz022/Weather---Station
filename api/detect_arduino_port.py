import serial.tools.list_ports
import serial

def get_arduino_port():
    ports = serial.tools.list_ports.comports()
    #print(ports)
    
    for port in ports:
        if "Arduino" in port.description or "USB-SERIA CH340" in port.description:
            '''
            print(f"Dectected port: {port.device}")
            print(f"Name: {port.name}")
            print(f"Description: {port.description}")
            print(f"HWID: {port.hwid}")
            print(f"PID: {port.vid}")
            print(f"Serial number: {port.serial_number}")
            print(f"Msnufacturer: {port.manufacturer}")
            print(f"Product: {port.product}")
            print(f"Interface {port.interface}")
            print(f"location: {port.location}")
            '''
            return port.device
    print("No Arduino port detected")
    return None

#Main
p = get_arduino_port()
print(p)
