from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.bind(('192.168.14.160',5268))
s.listen(5)
while True:
    new_s,addr = s.accept()
    content = new_s.recv(1024)
    print(content.decode())


