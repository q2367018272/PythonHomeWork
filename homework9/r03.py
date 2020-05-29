import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
s.connect((host, port))
while(True):
    sr=input('sr:')
    s.send(sr.encode('utf-8'))
    msg = s.recv(1024)
    print(msg.decode('utf-8'))
