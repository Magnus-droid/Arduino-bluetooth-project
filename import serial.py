import serial
import serial.tools.list_ports
from autodetect import *
aD = autoDetect()
print(aD)
ser = serial.Serial(aD, 9600, timeout=1)
ser.write(b'Board is ready!')   
data = ser.readline().decode("ascii")
print("Response: " + data)
"""while True:
    toSend = input('Send something to the board\n')
    ser.write(bytes(toSend, 'utf-8'))
    data = ser.readline().decode("ascii")
    print("Response: "+data)
    """


