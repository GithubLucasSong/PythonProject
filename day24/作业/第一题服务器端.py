# 1.基于tcp协议完成登录认证
#
#     客户端输入用户名密码
#     发送到服务端
#     服务端认证
#     发送结果到客户端


from socket import *
dic = {'songyu':'12345678'}
s = socket(AF_INET,SOCK_STREAM)
s.bind(('192.168.14.25',5268))
s.listen(5)
new_s,addr=s.accept()
new_s.send('请输入账号：'.encode())
name = new_s.recv(1024)
new_s.send('请输入密码：'.encode())
pwd = new_s.recv(1024)
if dic[name.decode()] == pwd.decode():
    new_s.send('登陆成功！'.encode())
else:
    new_s.send('登陆失败！'.encode())


