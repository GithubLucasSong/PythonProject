# # 2，看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
#
# class Foo(object):
#     a1 = 1
#     __a2 = 2
#
#     def __init__(self, num):
#         self.num = num
#         self.__salary = 1000
#
#     def show_data(self):
#         print(self.num + self.a1)
#
#
# obj = Foo(666)
#
# print(obj.num) #666
# print(obj.a1)  # 1
# print(obj.__salary) #无
# print(obj.__a2) #无
# print(Foo.a1) # 1
# print(Foo.__a2) # 无

# 3，看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】

# class Foo(object):
#     a1 = 1
#
#     def __init__(self, num):
#         self.num = num
#
#     def show_data(self):
#         print(self.num + self.a1)
#
#
# obj1 = Foo(666)
# obj2 = Foo(999)
# print(obj1.num) #666
# print(obj1.a1) #1
#
# obj1.num = 18 #
# obj1.a1 = 99
#
# print(obj1.num) #18
# print(obj1.a1) #99
#
# print(obj2.a1) #1
# print(obj2.num) #999
# print(obj2.num) #999
# print(Foo.a1)  #1
# print(obj1.a1) #99

# 4，看代码写结果，注意返回值。

# class Foo(object):
#
#     def f1(self):
#         return 999
#
#     def f2(self):
#         v = self.f1()
#         print('f2')
#         return v
#
#     def f3(self):
#         print('f3')
#         return self.f2()
#
#     def run(self):
#         result = self.f3()
#         print(result)
#
#
# obj = Foo()
# v1 = obj.run() #打印f3 f2 999
# print(v1)  #空

# #5，看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
#
# class Foo(object):
#
#     def f1(self):
#         print('f1')
#
#     @classmethod
#     def f2(cls):
#         print('f2')
#
#
# obj = Foo()
# obj.f1() #打印f1
# obj.f2() #打印f2
#
# Foo.f1() # 错误
# Foo.f2() #打印f2

# 6，看代码写结果

# class Department(object):
#     def __init__(self, title):
#         self.title = title
#
#
# class Person(object):
#     def __init__(self, name, age, depart):
#         self.name = name
#         self.age = age
#         self.depart = depart
#
#     def message(self):
#         msg = "我是%s,年龄%s,属于%s" % (self.name, self.age, self.depart.title)
#         print(msg)
#
#
# d1 = Department('人事部')
# d2 = Department('销售部')
#
# p1 = Person('武沛齐', 18, d1)
# p2 = Person('alex', 18, d1)
# p1.message() #我是武沛齐，年龄18，属于人事部
# p2.message() #我alex，年龄18，属于人事部


#7，尝试：在多进程中开启多线程

# from multiprocessing import Process
# import threading
# import time
# def func1():
#     print('进程1启动，准备启动线程')
#     def func1_1():
#         while True:
#             time.sleep(1)
#             print("进程1中的线程1执行")
#
#     def func1_2():
#         while True:
#             time.sleep(1)
#             print("进程1中的线程2执行")
#
#     t1 = threading.Thread(target=func1_1)
#     t2 = threading.Thread(target=func1_2)
#     t1.start()
#     t2.start()
#
#
#
# def func2():
#     print('进程2启动，准备启动线程')
#     def func2_1():
#         while True:
#             time.sleep(1)
#             print("进程2中的线程1执行")
#     def fun2_2():
#         while True:
#             time.sleep(1)
#             print("进程2中的线程2执行")
#
#     t1 = threading.Thread(target=func2_1)
#     t2 = threading.Thread(target=fun2_2())
#     t1.start()
#     t2.start()
#
# if __name__ =='__main__':
#     p1 = Process(target=func1)
#     p2 = Process(target=func2)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

#8，什么是C/S架构？,B/S
# C/S架构：客户端对服务器
# B/S架构：网页对服务器

#9，为何基于tcp协议的通信比基于udp协议的通信更可靠？
#udp是数据报协议，发送方只是将数据发送给接收方，并不能保证接收方一定收到了数据，会存在丢包状况。
#tcp是字节流协议，发送方和接收方在传输数据之前，会首先经过三次握手建立起稳定的连接通道，传输数据时，接收方每次接收到数据都会给发送方发送一
#个确认包，发送方接收到确认包之后才会继续传送下一个数据，数据传输过程中不会出现丢包状况，所以TCP比UDP更可靠

#10，流式协议指的是什么协议，数据报协议指的是什么协议？
#流协议：TCP
#数据报协议：UDP

#11，什么是socket？简述基于tcp协议的套接字通信流程
#socket中文含义为套接字，是用来数据传输的一个接口
#首先创建一个socket对象 :s = socket(AF_INET,SOCK_STREAM)，参数AD_INET代表IPV4协议，SOCK_STREAM代表TCP协议，
# 然后用s.connect(('192.168.14.25',5268))去连接目标IP地址和端口，建立连接之后就可以用s.send()和s.recv()收发数据了

#12，什么是粘包？ socket 中造成粘包的原因是什么？ 哪些情况会发生粘包现象？
#什么是粘包：字节流中的数据是首尾相接没有界限的，就像粘在一起，提取数据的时候如果不知道每条数据的界限，提取到的数据就会是粘在一起的不同数据的字节流
#socket 中造成粘包的原因是什么？：发送方发送的字节流长度和接收方提取的字节流长度不匹配
#哪些情况会发生粘包现象？ 比如发送方发送了很多条数据，由于字节流中的数据是没有界限的，这几条数据在字节流中是首尾相接的，接收方在
# 提取数据的时候，不知道每条数据的界限，一次提取的数据就会大于或者小于发送方发送的某一条数据，造成数据胡乱。

# 14，简述 TCP/IP 四层协议，七层协议
#四层：应用层 传输层 网络层 网络接口层
#七层：应用层 表达层 会话层 传输层 网络层 数据链路层 物理层

# 15，TCP 连接建立的时候 3 次握手，4次挥手的具体过程,其中的每一步具体在做什么(为什么是4次挥手,而不是3次)
#三次握手：第一次握手 客户端向服务器端发送一个SYN包 SYN包里随机携带一个数字X
#         第二次握手，服务器端收到SYN包，会把X数字加1，并发送一个携带X+1数字的ACK确认包返回给客户端,另外发送一个携带随机数字Y的SYN包给客户端
#         第三次握手,客户端收到ACK包，确认ACK里的数字是否为X+1,并把SYN包里的Y数字加1向服务器端发送一个新的ACK确认包，服务器端收到
#         ACK确认包，如果其中的数字为Y+1,那么服务器端和客户端就正式建立连接

#四次挥手：第一次挥手 调用close()的一方为主动关闭方，会向被动关闭方发送一个携带随机数字X的FIN包 此时主动关闭还可以接收数据
#         第二次挥手 被动关闭方接收到FIN包，然后向主动关闭方发送一个携带X+1的ACK确认包  此时被动关闭方还可以发送数据
#         第三次挥手 被动关闭方发送一个携带随机数字Y的FIN包，关闭传输通道。
#         第四次挥手 主动关闭方收到FIN包，并发送一个携带Y+1的ACK确认包， 被动关闭方接收到ACK包，确认数字为Y+1,至此双方四次挥手完成

#为什么是4次挥手,而不是3次：因为第二次挥手时，被动关闭方只是向主动关闭方传达一个‘我知道你要关闭了’，但是此时被动关闭方仍可以向主动关闭方
# 传送数据，当数据传送完成时，被动关闭方向主动关闭方第三次挥手，告诉主动关闭方‘数据传送完了’，主动关闭方收到第三次握手，然后第四次向被
# 动关闭方挥手，告诉被动关闭方‘我知道了’

#17，尝试分析TCP 为什么不是两次连接?而是三次握手?




#18，网络编程中设计并发服务器,使用多进程与多线程,请问有什么区别?
#多进程会比较占资源，但是有利于数据安全
#多线程节约资源，缺点是不利于数据安全
