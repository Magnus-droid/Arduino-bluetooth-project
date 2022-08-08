import serial

ser = serial.Serial("COM5", 9600, timeout=1)
ser.write(b'This is a test')
while True:
    data = ser.readline().decode("ascii")
    if data:
        print(data)