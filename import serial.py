import serial
import serial.tools.list_ports
from multiprocessing import Queue
from threading import Thread
from pathlib import Path

def portPinger(port, q):
    #print(port.name +": ", end='')
    ser = serial.Serial(port.name, 9600, timeout=2)
    ser.write(b'2')
    data = ser.readline().decode("ascii")
    q.put((data, port.name))

def autoDetect():
    if __name__ == "__main__":
        print("Scanning arduino port...\n")
        ports = serial.tools.list_ports.comports()
        ports.reverse()
        q = Queue()
        for port in ports:
            p = Thread(target=portPinger, args=(port,q), daemon=True)
            p.start()
            p.join(10.0)
            if p.is_alive():
               q.put((None, port.name))
            current = q.get_nowait()
            if current[0] == "Pong!":
                return current[1]


fle = Path('StorageTextFile.txt')
fle.touch(exist_ok=True)
with open('StorageTextFile.txt', 'r') as r:
    aD = r.read()  
    if aD == '':
        aD = autoDetect()
        with open('StorageTextFile.txt', 'w') as w:
            w.write(aD)
ser = serial.Serial(aD, 9600, timeout=1)
ser.write(b'Board found!')   
data = ser.readline().decode("ascii")
print("Response: " + data)
"""while True:
    toSend = input('Send something to the board\n')
    ser.write(bytes(toSend, 'utf-8'))
    data = ser.readline().decode("ascii")
    print("Response: "+data)
    """


