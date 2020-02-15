# 使用TCP协议编写一个能同时支持多个客户端访问的服务器


from socket import *
from multiprocessing import Process
import time

def per_client(new_socket,new_addr):
    while True:
        recvdata = new_socket.recv(1024)
        if len(recvdata) > 0:
            print('收到内容:{},客户端IP:{}'.format(recvdata.decode('utf-8'),new_addr))
        else:
            print(f'客户端:{new_addr}已关闭')
            break
    new_socket.close()

def main():
    sersocket = socket(AF_INET,SOCK_STREAM)
    sersocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    seraddr = ('',7777)
    sersocket.bind(seraddr)
    sersocket.listen(10)
    try:
        while True:
            print('服务器已启动')
            new_socket,new_addr = sersocket.accept()
            print('客户端访问')
            p = Process(target=per_client,args=(new_socket,new_addr))
            p.start()
            new_socket.close()
    finally:
            sersocket.close()
if __name__ == '__main__':
    main()

