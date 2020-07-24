# 一.TCP服务端
import socket

# 1.创建一个socket对象
sk = socket.socket()
# 2.绑定ip和端口号(在网络中注册主机)
sk.bind(("127.0.0.1", 9000))
# 3.开启监听
sk.listen()
# 4.建立三次握手
conn, addr = sk.accept()
# 5.收发数据的逻辑
print(conn.recv(1024))
conn.send(b"abc")  # 二进制字节流
# 6.四次挥手
conn.close()
# 7.退换端口
sk.close()