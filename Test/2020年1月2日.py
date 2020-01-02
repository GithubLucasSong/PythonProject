# import struct
# from socket import *
# filename = input('请输入要下载的文件名：')
# server_ip = '192.168.14.25'
# send_data = struct.pack('!H%dsb5sb'%len(filename),1,filename.encode(),0,'octet'.encode(),0)
# s = socket(AF_INET,SOCK_DGRAM)
# s.sendto(send_data,(server_ip,69)) #第一次发送，连接服务器69端口
# f = open(filename,'ab') #以追加模式打开
# while True:
#     recv_data = s.recvfrom(1024)
#     caozuoma,ack_num = struct.unpack('!HH',recv_data[0][:4]) #获取数据块编号
#     rand_port = recv_data[1][1] #获取服务器的随机端口
#     print(recv_data)
#     if int(caozuoma) == 5:
#         print('文件不存在')
#         break
#     print('操作码：%d,ACK:%d,服务器随机端口：%d，数据长度：%d'%(caozuoma,ack_num,rand_port,len(recv_data[0])))
#     f.write(recv_data[0][4:])
#     if len(recv_data[0]) < 516:
#         break
#     ack_data = struct.pack('!HH',4,ack_num)
#     s.sendto(ack_data,(server_ip,rand_port)) #回复ACK确认包

import struct
from socket import *
file_name = input('请输入要下载的文件名(带后缀名)：')
server_ip = '192.168.14.25'
send_data = struct.pack('!H%dsb5sb'%len(file_name),1,file_name.encode(),0,'octet'.encode(),0)
s = socket(AF_INET,SOCK_DGRAM)
s.sendto(send_data,(server_ip,69))
f = open(file_name,'ab')
while True:
    recv_data = s.recvfrom(1024)
    caozuoma,ack_num = struct.unpack('!HH',recv_data[0][:4])
    rand_port = recv_data[1][1]
    if int(caozuoma) == 5:
        print('找不到文件')
    print('操作码：{},ACK:{},服务器随机端口：{}，数据长度：{}'.format(caozuoma,ack_num,rand_port,len(recv_data[0])))
    f.write(recv_data[0][4:])
    if len(recv_data[0]) < 516:
        print('传输完成')
        break
    ack_data = struct.pack('!HH',4,ack_num)
    s.sendto(ack_data,(server_ip,rand_port))