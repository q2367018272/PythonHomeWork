import socket

def get_ip():
    host=socket.gethostname()
    ip = socket.gethostbyname(host)
    return ip



