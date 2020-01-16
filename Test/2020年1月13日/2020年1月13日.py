#类名操作静态属性
# class Human:
#     mind = '有思想'
#     dic = {}
#     l1 = []
#     def  work(self):
#         print('人类会工作')
#
# print(Human.__dict__)
# print(Human.mind)
# Human.mind = '无脑'
# print(Human.mind)
# del Human.mind
# Human.walk = '直立行走'
# print(Human.walk)

# class Human:
#     mind = '有思想'
#     dic = {}
#     l1 = []
#     def work(self):
#         print('人类会工作')
#     def tools(self):
#         print('人类会实用工具')
#
# Human.work(111)
# Human.tools(222)

# class Human:
#     mind = '有思想'
#     def work(self):
#         print('人类会工作')
#     def tools(self):
#         print('人类会使用工具')
# obj = Human()
# print(obj)

# class Human:
#     mind = '有思想'
#     language = '使用语言'
#     def __init__(self,name,sex,age,hobby):
#         self.n = name
#         self.s = sex
#         self.a = age
#         self.h = hobby
#
# obj = Human('meet','男',18,'运动')
# print(obj.n)

#对象查找属性的顺序：先从对象空间找----- 类空间找 ------父类空间找
#类名查找属性的顺序：先从本类空间找 -----父类空间找
#上面的顺序都是单向不可逆，类名不可能找到对象的属性
#对象查询对象中所有属性。对象.__dict__

# class Human:
#     mind = '有思想'
#     language = '使用语言'
#     def __init__(self,name,sex,age,hobby):
#         self.n = name
#         self.s = sex
#         self.a = age
#         self.h = hobby
#
# obj = Human('meet','男',18,'运动')
# print(obj.__dict__)

# class Human:
#     mind = '有思想'
#     language = '使用语言'
#     def __init__(self,name,sex,age,hobby):
#         self.n = name
#         self.s = sex
#         self.a = age
#         self.h = hobby
#
# obj = Human('meet','男',18,'运动')
# obj.job = 'IT'
# del obj.n
# obj.s = '女'
# print(obj.s)
# print(obj.__dict__)


# class Foo:
#     @property
#     def AAA(self):
#         print('get的时候运行我啊')
#
#     @AAA.setter
#     def AAA(self,value):
#         print('set的时候运行我啊{}'.format(value))
#
#     @AAA.deleter
#     def AAA(self):
#         print('delete的时候运行我啊')
#
# #只有在属性AAA定义property后才能定义AAA.setter,AAA.deleter
# f1=Foo()
# # f1.AAA
# f1.AAA='aaa'
# # del f1.AAA

# class A:
#     pass
#
# class B(A):
#     pass
#
# obj = B()
#
#
# print(isinstance(obj,B))
# print(isinstance(obj,A))


# name = 'ssss'
# age =19
# print('我是{a}年龄{b}'.format(b=age,a=name))
# print(f'我是{name}，年龄{age}')
#
# class A:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     def __hash__(self):
#         return hash(str(self.a)+str(self.b))
# a = A()
# print(hash(a))


# class Foo:
#     f = '类的静态变量'
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def say_hi(self):
#         print('hi,%s'%self.name)
#
# obj=Foo('egon',73)
#
# #检测是否含有某属性
# # print(hasattr(obj,'name'))
# # print(hasattr(obj,'say_hi'))
# #
# # n=getattr(obj,'name')
# # print(n)
# # func=getattr(obj,'say_hi')
# # func()
#
#
# setattr(obj,'show_name',lambda self:self.name+'sb')
# print(obj.__dict__)
# print(obj.show_name(obj))
#
# class Foo(object):
#
#     staticField = "old boy"
#
#     def __init__(self):
#         self.name = 'wupeiqi'
#
#     def func(self):
#         return 'func'
#
#     @staticmethod
#     def bar():
#         return 'bar'
#
# print(getattr(Foo, 'staticField'))
# print(getattr(Foo, 'func'))
# print(getattr(Foo, 'bar'))

import gevent
def A():
    while True:
        print(".........A.........")
        gevent.sleep(1)#用来模拟一个耗时操作
        #gevent中：当一个协程遇到耗时操作会自动交出控制权给其他协程
def B():
    while True:
        print(".........B.........")
        gevent.sleep(1)#每当遇到耗时操作，会自用转到其他协程
g1 = gevent.spawn(A) # 创建一个gevent对象（创建了一个协程），此时就已经开始执行A
g2 = gevent.spawn(B)
g1.join()  #等待协程执行结束
g2.join()  #会等待协程运行结束后再退出


