import socket
import sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
serversocket.bind((host, port))
serversocket.listen(5)
clientsocket, addr = serversocket.accept()
while True:
    print("连接地址: %s" % str(addr))
    print(clientsocket.recv(1024))
    msg = input('sr:')
    clientsocket.send(msg.encode('utf-8'))