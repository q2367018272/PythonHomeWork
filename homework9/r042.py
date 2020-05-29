import socket
import threading
import os
from r04 import get_ip
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = (get_ip(),8888)
s.connect(addr)

def recv():
    print('连接成功-接收消息')
    while True:
        try:
            res=s.recv(1024)
            print(res.decode('utf-8'))
        except ConnectionResetError:
            print('服务器关闭')
            s.close()
            break
    os._exit(0)

def send():
    print('连接成功-传送消息')
    print('输入esc退出')
    while True:
        time.sleep(0.1)
        msg=input('sr:')
        if msg =="esc":
            print('退出成功')
            s.close()
            break
        s.send(msg.encode('utf-8'))
    os._exit(0)

if __name__=='__main__':
    try:
        th1=threading.Thread(target=send)
        th2=threading.Thread(target=recv)
        th2.start()
        th1.start()
    except ConnectionRefusedError:
        print('重新连接')


