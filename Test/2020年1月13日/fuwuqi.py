from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.bind(('',5268))
s.listen(5)
new_s,addr = s.accept()
f = open('2020年1月13日.html','r',encoding='utf-8')
data = f.read()
re_s = new_s.recv(1024)
print(re_s)
new_s.send(b'HTTP/1.1 200 OK\r\n\r\n')
new_s.send(data.encode())



class cls:
    dic = []
    def


cls.dic.append()
cls.dic

c = cls()
c2 = cls()
c.dic.append(1)
print(c2.dic)
