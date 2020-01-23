


# def __init__()  实例化的时候触发


# def len()

# class  A():
#     def __init__(self,name):
#         print('实例化的时候触发我')
#         self.name = name
#
#     def __len__(self):
#         print('执行len触发我')
#         return len(self.name)
#
#
#
# a = A('Alex')
# print(len(a))

# class A(object):
#     def __hash__(self):
#         return  1110101
#
# a = A()
# print(hash(a))


# class A():
#
#     def __str__(self):
#         return '格式化的时候执行我'
#
# a = A()
# print(a) # print触发的就是str



# class A():
#     def __str__(self):
#         return '格式化的时候执行我'
#     def __repr__(self):
#         return '执行的我'
#
# a = A()
# print(a) # print的时候优先执行str，str比repr优先级高。



# class A():
#     def __call__(self, *args, **kwargs):
#         print('执行到我了')
#         self.func()   #当类中有__call__方法 ，对象名就支持直接加括号
#
#     def func(self):
#         print('啦啦啦')
#
# a = A()
# a()
# a.func()



# class A():
#
#     def __init__(self,a):
#         self.a = a
#
#     def __add__(self, other):
#         return self.a + other.a
#
#
# a = A(10)
# b = A(20)
#
# print(a + b)



#
# class A():
#     def __init__(self,name):
#         self.name = name
#
#     def __del__(self):
#         print('删除的时候执行我')
#
#
# a = A('alex')
# del a.name


# class A():
#
#     def __init__(self,name): # 给空间封装东西的
#         print('我是init')
#         self.name = name
#
#     def __new__(cls, *args, **kwargs): #开辟空间的
#         print('我是New')
#
#     def show(self):
#         print(self.name)
#
# a = A('alex')
# a1 = A('alex')
# a2 = A('alex')
# a3 = A('alex')
#
# a.show()
# a1.show()


class A():

    __a = None

    def __init__(self,name): # 给空间封装东西的
        print('我是init')
        self.name = name

    def __new__(cls, *args, **kwargs): #开辟空间的
        if not cls.__a:
            a = cls.__new__(cls, *args, **kwargs) # 让父类开辟空间

    def show(self):
        print(self.name)


a = A('alex')
print(a.name)
