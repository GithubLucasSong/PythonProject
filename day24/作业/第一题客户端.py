from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.connect(('192.168.14.25',5268))
print('连接服务器成功！')
data = s.recv(1024)
print(data.decode())
name = input()
s.send(name.encode())
data1 = s.recv(1024)
print(data1.decode())
pwd = input()
s.send(pwd.encode())
data2 = s.recv(1024)
print(data2.decode())


