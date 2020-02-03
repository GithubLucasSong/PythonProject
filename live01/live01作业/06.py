# 6，命名空间四件套
# 读程序, 标出程序的执行过程, 画出内存图解, 说明答案和为什么
# 请不要想当然, 执行之后检查结果然后再确认和自己的猜想是不是一致
# (1)


class A:
    Country = '中国'
    def __init__(self, name, age, country):
        self.name = name
        self.age = age

    def func1(self):
        print(self)

a = A('alex', 83, '印度')
b = A('wusir', 74, '泰国')
A.Country = '英国'
a.Country = '日本'
print(a.Country) # 日本
print(b.Country) # 英国
print(A.Country) # 英国
# b.

class A:
    Country = '中国'
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.Country = country

    def func1(self):
        print(self)

a = A('alex', 83, '印度')
b = A('wusir', 74, '泰国')
A.Country = '英国'
a.Country = '日本'
print(a.Country) # 日本
print(b.Country) # 泰国
print(A.Country) # 英国
c.

class A:
    Country = '中国'
    def __init__(self, name, age, country):
        self.name = name
        self.age = age

    def Country(self):
        return self.Country

a = A('alex', 83, '印度')
b = A('wusir', 74, '泰国')
print(a.Country)  # 内存地址
print(a.Country()) # 内存地址