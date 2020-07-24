# TCP 客户端
import socket

# 1.创建一个socket对象
sk = socket.socket()
# 2.与服务器进行连接
sk.connect(("127.0.0.1", 9000))
# 3.收发数据
sk.send(b'abc')
print(sk.recv(1024))
# 4.关闭连接
sk.close()
