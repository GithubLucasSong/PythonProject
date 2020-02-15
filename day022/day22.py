# from socket import *
# s = socket(AF_INET,SOCK_DGRAM) #创建套接字
# addr = ('192.168.14.25',8080)  #准备接收方地址
# data = input('请输入：')
# s.sendto(data.encode(),addr)
# #发送数据时，python3需要将字符串装换成byte
# #encode('utf-8') 用utf-8对数据进行编码，获得bytes类型对象
# #decode()反过来
# s.close()

# from socket import *
# import time
#
# s = socket(AF_INET,SOCK_DGRAM) #创建套接字
# s.bind(('', 8788))
# addr = ('192.168.14.25',8788) #准备接收方地址
# data = input('亲输入：')
# s.sendto(data.encode(),addr)
# time.sleep(1)
# #等待接收数据
# data = s.recvfrom(1024)
# # 1024表示本次接收的最大的字节数
# print(data)


from socket import *
#创建套接字
udpSocket = socket(AF_INET,SOCK_DGRAM)
#绑定本地信息，不使用随机分配的端口
binAddr = ('',7088)
udpSocket.bind(binAddr)
num = 0
while True:
    #接收对方发送的数据
    recvData = udpSocket.recvfrom(1024)
    print(recvData)
    #将接收到的数据发回给对方
    udpSocket.sendto(recvData[0],recvData[1])
    num += 1
    print('已将接收到的第%d个数据返回给对方,'%num)
udpSocket.close()