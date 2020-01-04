#13，基于tcp socket，开发简单的远程命令执行程序，允许用户执行命令，并返回结果

from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.connect(('192.168.14.25',5268))
print('连接服务器成功！')
cmd = input('请输入命令：')
s.send(cmd.encode())
data = s.recv(1024)
print(data.decode())
print('显示完成！')