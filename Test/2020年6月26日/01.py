# s = 'asdsadad'
# r = reversed(s)
# print(r)

# a = 'alex'
# # b=a.encode('utf8')
# # print(a)
# # print(b)
# #
# #
# # def show(name,age):
# #     """
# #
# #     :param name:
# #     :param age:
# #     :return:
# #     """

#
# def fun(x):
#     if x>0:
#         fun(x-1)  # fun(0)
#         print(x)
#
# fun(1)


# list = [1,
#  2,
#  6,
#  7,
#  5,
#  7,
#  8,
#  9,
#  3,
#  2,]
#
# for i in list:
#     print('hello')


# def wrapper(func):
#     def inner(*args, **kwargs):
#         print('函数开始执行')
#         a = func(*args, **kwargs)
#         print('函数执行完毕')
#         return a
#
#     return inner
#
#
# @wrapper
# def index():
#     print('执行中')
# index()


# def x(counter):
#     list = []
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             print('函数开始执行')
#             for i in range(counter):
#                 a = func(*args, **kwargs)
#                 list.append(a)
#             print('函数执行完毕')
#             return list
#
#         return inner
#
#     return wrapper
#
#
# @x(3)
# def index():
#     print('执行中')
#     return 999
# print(index())


# head = {
#     next: ['下一个']
# }
#
# current_node = head
# next_node = head[next]
#
# head[next] = ['上一个']
# # head[next][0] = '上一个'
#
#
# current_node = next_node
#
# print(current_node)


# a = [123]
# b = a
# a = [456]
# # a[0] = 456
# print(b)


# import struct
#
# res = struct.pack('i',2100000)
# print(res)
# res2 = struct.unpack('i',res)
# print(res2)


# # 一.TCP服务端
# import socket
#
# # 1.创建一个socket对象
# sk = socket.socket()
# # 2.绑定ip和端口号(在网络中注册主机)
# sk.bind(("127.0.0.1", 9000))
# # 3.开启监听
# sk.listen()
# # 4.建立三次握手
# conn, addr = sk.accept()
# # 5.收发数据的逻辑
# conn.recv(1024)
# conn.send(b"abc")  # 二进制字节流
# # 6.四次挥手
# conn.close()
# # 7.退换端口
# sk.close()
#
# # TCP 客户端
# import socket
#
# # 1.创建一个socket对象
# sk = socket.socket()
# # 2.与服务器进行连接
# sk.connect(("127.0.0.1", 9000))
# # 3.收发数据
# sk.send(b'abc')
# sk.recv(1024)
# # 4.关闭连接
# sk.close()
#
# # 二.UDP服务端
# import socket
#
# # 1.创建一个socket对象
# sk = socket.socket(type=socket.SOCK_DGRAM)
# # 2.绑定ip和端口号(在网络中注册主机)
# sk.bind(("127.0.0.1", 9000))
# # 3.收发数据的逻辑
# msg, cli_addr = sk.recvfrom(1024)  # 必须要先接受数据
# sk.sendto(b'abc', cli_addr)
# # 4.关闭连接
# sk.close()
#
# # UDP客户端
# import socket
#
# # 1.创建一个socket对象
# sk = socket.socket(type=socket.SOCK_DGRAM)
# # 2.收发数据的逻辑
# sk.sendto(b'abc', ("127.0.0.1", 9000))  # 必须要发数据
# msg, cli_addr = sk.recvfrom(1024)
# # 3.关闭连接
# sk.close()
#
# # 三.TCP / socketserver 支持TCP的并发连接
# import socketserver
#
#
# class MyServer(socketserver.BaseRequestHandler):
#     def handle(self):
#         # 三次握手的连接对象
#         conn = self.request
#
#
# if __name__ == "__main__":
#     server = socketserver.ThreadingTCPServer(("127.0.0.1", 9000), MyServer)
#     server.serve_forever()
#     # (sk.setsockopt允许端口重用, 测试环境可以用;)


# def producer():
#     for i in range(100):  # 0 1 2 3 4 5 6 ....
#         n = yield i
#         print("结果:", n)
#
#
# def consumer():
#     # 初始化当前生成器函数
#     g = producer()
#     # send可以类比next,第一次调用时,必须发送None,send给yield发送数据(上一个yield)
#     print(g.send(None))
#     for i in range(10):  # 0 1 2 3 ... 9
#         res = g.send(i)
#         print(res)
#
#
# consumer()

# import time
#
#
# def producer():
#     for i in range(100):  # 0 1 2 3 4 5 6 ....
#         print('生成器接受到请求')
#         n = yield i
#         print('开始睡眠')
#         time.sleep(2)
#         print("结果:", n)
#         print('睡眠结束')
#
#
# die = producer()
# print('准备发送None')
#
# print(die.send(None))
# print('发送None完成')
#
# time.sleep(3)
# print('准备发送9')
#
# print(die.send('jiu'))
# print('发送9完成')

#
# from threading import Lock
#
# 死锁, 互斥锁, 递归锁
# 死锁: 只上锁不解锁是死锁
# 例:
# (1)
# lock = Lock()
# lock.acquire()

# print(1111)

# # (2)
# 线程1
# a = Lock()
# b = Lock()
# a.acquire()
# b.acquire()
#
# 线程2
# b.acquire()
# a.acquire
#
# 线程1, 拿着a锁枪b锁
# 线程1, 拿着b锁枪a锁
# 出现逻辑死锁
#
# # (3)递归锁,用来解决线上死锁现象;
# a = b = RLock()
# a.acquire()
# a.acquire()
#
# a.release()
# a.release()
#
# # 如何避免:
# 使用一把锁, 尽量不要使用锁嵌套, 避免发生逻辑上的死锁,
# 如果出现死锁现象, 可以快速用递归锁解决


# import threading
# import time
#
# def _wait():
#     time.sleep(60)
# # flag a
# t = threading.Thread(target=_wait)
# t.setDaemon(False)
# t.start()
# # flag b
# t1 = threading.Thread(target=_wait)
# t1.setDaemon(False)
# t1.start()

# 守护进程 , 守护线程
# 守护进程: 守护的是主进程(当主进程代码执行结束后,会立刻杀死守护进程)
# 守护线程: 守护的是所有线程(等所有线程都执行结束了之后,守护线程才会自动终止)

# import threading
# import time
#
#
# def _wait():
#     time.sleep(60)
#     print('123')
# # flag a
# print('a')
# t = threading.Thread(target=_wait)
# t.setDaemon(True)
# # t.start()
# # flag b
# print('b')

# import threading
#
# loop = int(1E7)
#
#
# def _add(loop: int = 1):
#     global number
#     for _ in range(loop):
#         number += 1
#
#
# def _sub(loop: int = 1):
#     global number
#     for _ in range(loop):
#         number -= 1
#
#
# number = 0
# ta = threading.Thread(target=_add, args=(loop,))
# ts = threading.Thread(target=_sub, args=(loop,))
# ta.start()
# ta.join()
# ts.start()
# ts.join()
# print(number)

# print(int(1E7))


# import threading
# loop = int(1E7) # 10000000.0
# def _add(loop:int = 1):
# 	global number
# 	for _ in range(loop):
# 		number += 1
#
# def _sub(loop:int = 1):
# 	global number
# 	for _ in range(loop):
# 		number -= 1
# number = 0
# ta = threading.Thread(target=_add,args=(loop,))
# ts = threading.Thread(target=_sub,args=(loop,))
# ta.start()
# ts.start()
# ta.join()
# ts.join()
# print(number)


# sql = "select * from user_pwd where username='%s',password='%s'"
#
#
# asdadasdasda' or 1=1 -- sadada
#
# sql = "select * from user_pwd where username='asdadasdasda' or 1=1 -- sadada',password='%s'"


import random


def func1():
    all_test = []
    for i in range(1000):
        once_test = []
        for j in range(10):
            once_test.append(random.choices('力耐敏体魔')[0])
        # print(once_test)
        all_test.append(once_test)
    success_percent = 0
    for one in all_test:
        if one.count('耐') <= 2:
            success_percent += 1
    print('一次性合成10点属性耐不超过2的几率是：%.1f%%' % (success_percent / 1000 * 100))


def func2():
    all_test = []
    for i in range(1000):
        once_test = []
        for j in range(4):
            once_test.append(random.choices('力耐敏体魔')[0])
        # print(once_test)
        all_test.append(once_test)

    success_percent = 0
    for one in all_test:
        if one.count('耐') <= 1:
            success_percent += 1
    print('一次性合成4点属性(两只精灵)耐不超过1的几率是：%.1f%%' % (success_percent / 1000 * 100))


def func3():
    all_test = []
    for i in range(1000):
        once_test = []
        for j in range(4):
            once_test.append(random.choices('力耐敏体魔')[0])
        # print(once_test)
        all_test.append(once_test)

    success_percent = 0
    for one in all_test:
        if one.count('耐') <= 2:
            success_percent += 1
    print('一次性合成4点属性(两只精灵)耐不超过2的几率是：%.1f%%' % (success_percent / 1000 * 100))


def func4():
    all_test = []
    for i in range(1000):
        once_test = []
        for j in range(4):
            once_test.append(random.choices('力耐敏体魔')[0])
        # print(once_test)
        all_test.append(once_test)

    success_percent = 0
    for one in all_test:
        if one.count('耐') <= 2:
            success_percent += 1
    print('一次性合成4点属性(两只精灵)耐不超过2的几率是：%.1f%%' % (success_percent / 1000 * 100))


def func5():
    all_test = []
    for i in range(1000):
        once_test = []
        for j in range(4):
            once_test.append(random.choices('力耐敏体魔')[0])
        # print(once_test)
        all_test.append(once_test)

    success_percent = 0
    for one in all_test:
        if one.count('耐') == 0:
            success_percent += 1
    print('一次性合成4点属性(两只精灵)耐为0的几率是：%.1f%%' % (success_percent / 1000 * 100))

def func6():
    all_test = []
    for i in range(1000):
        once_test = []
        for j in range(6):
            once_test.append(random.choices('力耐敏体魔')[0])
        # print(once_test)
        all_test.append(once_test)

    success_percent = 0
    for one in all_test:
        if one.count('耐') == 0:
            success_percent += 1
    print('一次性合成6点属性(三只精灵)耐为0的几率是：%.1f%%' % (success_percent / 1000 * 100))

def func7():
    all_test = []
    for i in range(1000):
        once_test = []
        for j in range(6):
            once_test.append(random.choices('力耐敏体魔')[0])
        # print(once_test)
        all_test.append(once_test)

    success_percent = 0
    for one in all_test:
        if one.count('耐') <= 1:
            success_percent += 1
    print('一次性合成6点属性(三只精灵)耐不超过1的几率是：%.1f%%' % (success_percent / 1000 * 100))
def func8():
    all_test = []
    for i in range(1000):
        once_test = []
        for j in range(6):
            once_test.append(random.choices('力耐敏体魔')[0])
        # print(once_test)
        all_test.append(once_test)

    success_percent = 0
    for one in all_test:
        if one.count('耐') >= 2:
            success_percent += 1
    print('一次性合成6点属性(三只精灵)耐超过2几率是：%.1f%%' % (success_percent / 1000 * 100))


func1()
func2()
func3()
func4()
func5()
func6()
func7()
func8()

