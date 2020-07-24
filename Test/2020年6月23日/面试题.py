# # lst = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 32769, 65536, 4294967296]
# #
# # # 输 出
# # {
# #     [1, 2, 3, 8],
# #     [16, 32, 64],
# #     [128, 256, 512],
# #     [1024, ],
# #     [32769, 65536],
# #     [4294967296],
# # }
#
#
# # import copy
# # lst1 = [1,2,3]
# #
# # print(lst1[::])
#
#
# # import copy
# #
# # a = [1, 2, 4, 5, ['b', 'c']]
# # b = a
# # c = copy.copy(a)
# # d = copy.deepcopy(a)
# # a.append(5)
# # a[4].append("d")
# # print(b)
# # print(c)
# # print(a)
#
#
# # a = b = 1
# # for i in range(10):
# #     print(a)
# #     a, b = b, a+b #1 2
#
#
# # def fib(n):
# # 	if n <= 2:
# # 		return 1
# # 	# 现在值 = 上一个值 + 上上个值
# # 	return fib(n-1) + fib(n-2)
# # # 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# # print(fib(5))
#
#
# # a,b = 0,1
# # for i in range(10):
# #     print(b)
# #     a, b = b, a+b
#
#
# # def fib(n):
# # 	if n <= 2:
# # 		return 1
# # 	# 现在值 = 上一个值 + 上上个值
# # 	return fib(n-1) + fib(n-2)
# # # 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# # c
#
# # 第一种
# # f = open('etl_log.txt',mode="r",encoding="utf-8")
# # for i in range(10):
# #     print(f.readline())
#
#
# # a = 123
# # def func():
# #     global a
# #     a +=1
# #     print(a)
# #
# # func()
# #
# # lst = [1, 2, 3, 43, 5, 6]
# # f = filter(lambda x: True if x % 2 == 0 else False, lst)
# # print(f)
#
#
# # map -> 处理计算数据[一次计算1个]
# # lst = [1,2,3]
# # it = map(lambda x : x*3 , lst)
# # print(list(it))
#
#
# # from functools import reduce
# # # reduce -> 计算数据[一次计算2个]
# # lst = [5,6,7,8] # => int 5678
# # res = reduce(lambda x,y : x*10 + y , lst)
# # print(res)
#
#
# # a= dict(zip(('a','b','c','d','e',),(1,2,3,4,5,)))
# # it = enumerate(["a","b"] , start=10)
# # print(dict(it))
#
#
# # list = [123]
# #
# # def func(*args, **kwargs):
# #     print(args)
# #
# #
# # def func2():
# #     a = 123
# #     b = 456
# # func(list[0])
#
#
# #
#
# # def a(*args):
# #     def wrapper(func):
# #         def inner(*args,**kwargs):
# #             print('运行之前')
# #             ret = func(*args,**kwargs)
# #             print('运行之后')
# #         return inner
# #     return wrapper
# #
# # @a(123)
# # def func():
# #     print('运行')
# #
# #
# #
# #
# # func()
#
#
# 标准版装饰器

# def wrapper(func):
#     def inner(*args, **kwargs):
#         print('运行之前')
#         ret = func(*args, **kwargs)
#         print('运行之后')
#
#     return inner
#
#
# @wrapper
# def func():
#     print(args[0])
#     print('运行')
#
#
# func(5)


#
#
# # 带参数装饰器
# def a(x):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             print('参数是:', x)
#             print('运行之前')
#             ret = func()
#             print('运行之后')
#
#         return inner
#
#     return wrapper
#
#
# @a(3)
# def func():
#     print('运行')
#
#
# func()
#
#
# def wrapper(func):
#     def inner(*args, **kwargs):
#         print('运行之前')
#         ret = func()
#         print('运行之后')
#
#     return inner
#
#
# @wrapper
# def func():
#     print('运行')
#
#
# func()


# def num():
#     return [lambda x: i * x for i in range(4)] # [lambda x: 3 * x，lambda x: 3 * x，lambda x: 3 * x，lambda x: 3 * x ]
#
#
# print([m(2) for m in num()])
#
# def func(a, b=[]):
#     b.append(1)
#     print(a, b)
#
#
# func(a=2)
# func(2)
# func(2)

# a = 123
# d = {a:'223'}
# print(d[a])
# print(a)


# def func(a, b=[]):
#     b.append(a)
#     return b
#
#
# v1 = func(1)
# v2 = func(2, [10, 20])
# v3 = func(3)
# print(v1, v2, v3)
#
# ip = '10.3.9.12'
#
# def transform_ip():
#     ip_list = ip.split('.')
#     bin_list = []
#     for i in ip_list:
#         bin_list.append('%08s' % bin(int(i)))
#     print(bin_list)
#
# transform_ip()

#
# ip = '10.3.9.12'
#
#
# def transform_ip():
#     bin_list = []
#     for i in ip.split('.'):
#         num = bin(int(i)).strip('0b')
#         bin_list.append('{:0>8s}'.format(num))
#     bin_str = ''.join(bin_list)
#     print(bin_str)
#     print(int(bin_str, base=2))
#
#
# transform_ip()

# ip = '10.3.9.12'
#
# def transform_ip():
#     ip_list = ip.split('.')
#     bin_list = []
#     for i in ip_list:
#         bin_list.append('{0:08d}'.format(1))
#     print(bin_list)
#
# transform_ip()


# ip = '10.3.9.12'
#
# def transform_ip():
#     ip_list = ip.split('.')
#     bin_list = []
#     for i in ip_list:
#         bin_list.append('{:0>8d}'.format(1))
#     print(bin_list)
#
# transform_ip()

# print('{:08b}'.format(3))    # 00000011   # 10进制数字转换成二进制数字
# print('{:0>8s}'.format('3')) # 00000003   # 字符串格式
# print('%08d' % 3 )           # 00000003   # 数字格式
# print('%8s' % '3')           #        3   # 字符串格式只能空格部位
# print(format(3, "08d"))      # 00000003   # 数字格式
# print(format(3, "08b"))      # 00000011   # 10进制数字转换成二进制数字
# print(format('3', "0>8s"))   # 00000003   # 字符串格式
# print('3'.rjust(8,'0'))      # 00000003   # 字符串格式

# 方法1
# ip = '10.3.9.12'
#
#
# def transform_ip():
#     ip_list = ip.split('.')
#     bin_list = []
#     for i in ip_list:
#         num = bin(int(i)).lstrip('0b')
#         print(i, '----------', num)
#         bin_list.append('{:0>8s}'.format(num))
#     bin_str = ''.join(bin_list)
#     print(int(bin_str, base=2))
#
#
# transform_ip()

# 方法一
# ip = "10.3.9.12"
# strvar = ''
# for i in ip.split("."):
#     # print(i)
#     bin_str = str(bin(int(i)))[2:]
#     strvar += bin_str.rjust(8, "0")
#     print(strvar)
#
# # 把二进制字符串转换成十进制
# print(int(strvar, 2))
#
# 方法二
# ip = "10.3.9.12"
# strvar = ""
# for i in ip.split("."):
#     # print(format(int(i),"08b"))
#     # 8总长度 0用来补齐8位的 b代表二进制;
#     strvar += format(int(i), "08b")
# print(strvar)  # 00001010000000110000100100001100
# print(int(strvar, 2))  # 167971084


# import math
# print(math.floor(5.5))
# print(math.ceil(5.1))
# import re
# # print(re.match(r'sy','00000sy000sy0000')) # None
# # print(re.search(r'sy','00000sy000sy0000')) # <_sre.SRE_Match object; span=(5, 7), match='sy'>
#
#
# # .? 和 .* 和.*?的区别
# print(re.findall ('m.?e','m-e-me-meet-m00000e-m0e0'))  # ['m-e', 'me', 'mee', 'm0e']
# print(re.findall ('m.*e','m-e-me-meet-m00000e-m0e0'))  # ['m-e-me-meet-m00000e-m0e']
# print(re.findall ('m.*?e','m-e-me-meet-m00000e-m0e0')) # ['m-e', 'me', 'me', 'm00000e', 'm0e']

# import random
# print( random.randrange(1,100,2) )


from threading import Lock


# class SingleTon():
#     # 防止类外直接调用__obj成员,对他进行保护,所以用私有
#     __obj = None
#     lock = Lock()
#
#     # 控制对象的创建
#     def __new__(cls, *args, **kwargs):
#         with cls.lock:
#             if not cls.__obj:
#                 cls.__obj = object.__new__(cls)
#             return cls.__obj
#
#
# obj1 = SingleTon()
# obj2 = SingleTon()
# obj3 = SingleTon()
# print(id(obj1), id(obj2), id(obj3))


# class XXX():
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def __new__(cls, *args, **kwargs):
#
#
# class CCC(XXX):
#     def __init__(self):
#         pass
#
#     XXX.func()
#
#
# C = CCC()


# class Parent(object):
#     x = 1
#
#
# class Child1(Parent):
#     pass
#
#
# class Child2(Parent):
#     pass
#
#
# print(Parent.x, Child1.x, Child2.x) # 1 1 1
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x) # 1 2 1
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x) # 3 2 3

#
# """ 面向对象的上下文管理, with语法的具体实现 """
#
#
# class Context:
#     # 在使用with语法时,自动触发,功能返回对象
#     def __enter__(self):
#         return self
#
#     # 在执行完with语法之后,自动触发,用来做收尾操作
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("关闭文件 f.close() ")
#
#     def do_something(self):
#         print("我是做点什么~")
#
#
# with Context() as ctx:
#     ctx.do_something()
# lst = [1,2,3,4,5,5,5,5,5,8,8,5,5,5,]
# lst.sort()
# print(lst)

# a= 100
# b =a
# del a
# del b
# print(b)


class Node():
    def __init__(self, value, next):
        self.value = value
        self.next = next


head = Node('头', None)
prev = head

for i in range(5):
    node = Node('节点%d' % i, None)
    prev.next = node
    prev = node


# 查看链表关系
# print(head.value)
# print(head.next.value)
# print(head.next.next.value)
# print(head.next.next.next.value)
# print(head.next.next.next.next.value)
# print(head.next.next.next.next.next.value)
# print(head.next.next.next.next.next.next)


def reverse_link_list(head):
    if not head.next:
        return head
    prev_node = None
    current_node = head
    next_node = head.next

    while 1:

        current_node.next = prev_node
        if not next_node:
            break
        # 重置
        prev_node = current_node
        current_node = next_node #  next_node已经取出
        next_node = current_node.next

    return current_node


last = reverse_link_list(head)
print(last.value)
print(last.next.value)
print(last.next.next.value)
print(last.next.next.next.value)
print(last.next.next.next.next.value)
print(last.next.next.next.next.next.value)
