# import re
#
# res = re.findall ('s.*?y','sy-s1y-s11y-s111y')
# res = re.search('<a>(?P<cont>.+)</a>','<a>sy</a>')
#
#
#
#
# print(res.group(1))
#


# print(
#     1 or 2 ,
#     3 and 7 or 9 and 0,
#     1 or 3,
#     1 and 3,
#     0 and 2 and 1,
#     0 and 2 or 1,
#     0 and 2 or 1 or 4,
# ),


# with open('db.txt','r',encoding='utf-8') as f:
#     while 1:
#         if f.readline() == '':
#             break
#         print(f.readline())


# x=10
# print(x+=x-=x-x)

# a = [1,2,3]
# b = a
# b.append(4)
# print(a)

from socket import *
from multiprocessing import *
from time import sleep
from threading import Thread


# 处理客户端的请求并为其服务
def dealWithClient(newSocket, destAddr):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData) > 0:
            print('recv[%s]:%s' % (str(destAddr), recvData))
        else:
            print('[%s]客户端已经关闭' % str(destAddr))
            break
    newSocket.close()


def main():
    serSocket = socket(AF_INET, SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    localAddr = ('', 7788)
    serSocket.bind(localAddr)
    serSocket.listen(5)

    try:
        while True:
            print('-----主进程， ， 等待新客户端的到来------')
            newSocket, destAddr = serSocket.accept()
            print('-----主进程， ， 接下来创建⼀个新的线程负责数据处理', str(destAddr))
            client = Thread(target=dealWithClient, args=(newSocket, destAddr))
            client.start()
            # 因为线程中共享这个套接字， 如果关闭了会导致这个套接字不可用
            # 但是此时在线程中这个套接字可能还在收数据， 因此不能关闭
            # newSocket.close()
    finally:
        serSocket.close()


if __name__ == '__main__':
    main()
