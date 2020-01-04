from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.connect(('192.168.14.25',7788))
while True:
    info = input(':')
    s.send(info.encode())
    data = s.recv(1024)
    print(data.decode())
    if str(info) == 'close':
        s.close()

