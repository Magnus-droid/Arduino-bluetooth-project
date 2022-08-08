import serial
import serial.tools.list_ports
from multiprocessing import Queue
from time import sleep
from threading import Thread



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


print(autoDetect())
