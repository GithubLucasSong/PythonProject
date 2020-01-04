from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.bind(('192.168.14.25',5268))
s.listen(5)
new_s,addr = s.accept()
data = new_s.recv(1024)
print(data.decode())
new_s.send('你也好'.encode())