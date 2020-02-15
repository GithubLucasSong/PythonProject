from threading import Thread
from socket import *
import threading
import time
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('',7777))
addr = ('192.168.1.7',8888)

def func1():
    while True:
        data = input()
        s.sendto(data.encode(),addr)


def func2():
    while True:
        redata = s.recvfrom(1024)
        print(f'内容：{redata[0].decode()}\n时间:{time.ctime()}')


if __name__ == '__main__':
    t1 = Thread(target=func1)
    t2 = Thread(target=func2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()