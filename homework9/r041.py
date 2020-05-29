from r04 import get_ip
import socket
import threading
import os

class ChatSever:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (get_ip(), 8888)
        self.users = {}

    def start(self):
        try:
            self.sock.bind(self.addr)
        except Exception as e:
            print(e)
        self.sock.listen(5)
        print('服务器开启，输入stop关闭')
        self.accept()

    def accept(self):
        while True:
            sock,addr=self.sock.accept()
            self.users[addr]=sock
            print("用户{}连接成功！现在共有{}位用户".format(addr, len(self.users)))
            threading.Thread(target=self.recv,args=(sock,addr)).start()

    def recv(self,sock,addr):
        while True:
            try:
                res=sock.recv(1024).decode('utf-8')
                msg = "用户{}发来消息：{}".format(addr, res)
                for c in self.users.values():
                    c.send(msg.encode('utf-8'))
            except ConnectionResetError:
                print("用户{}已经退出聊天！".format(addr))
                self.users.pop(addr)
                break
    def close(self):
        for c in self.users.values():
            c.close()
        self.sock.close()
        os._exit(0)

if __name__=='__main__':
    sever=ChatSever()
    th1=threading.Thread(target=sever.start)
    th1.start()
    while True:
        cmd=input()
        if cmd == "stop":
            sever.close()
        else:
            print('重新输入')
