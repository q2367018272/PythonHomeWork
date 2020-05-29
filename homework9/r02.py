from socket import *
'''
udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dest_addr = ('192.168.0.6',8080)
send_data = input("请输入要发送的数据:")
udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
udp_socket.close()
'''

udp_socket = socket(AF_INET, SOCK_DGRAM)
local_addr = ('192.168.0.6', 8080)
udp_socket.bind(local_addr)
recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
print(recv_data)
udp_socket.close()
