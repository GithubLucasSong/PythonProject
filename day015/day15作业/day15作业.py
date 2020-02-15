# 1.定义一个学生类
# 类变量为:
#
# 姓名
# 年龄
# 成绩 [语文,数学,英语]
# 实例方法为:
# 获取学生的姓名：get_name() 返回类型:str
# 获取学生的年龄：get_age() 返回类型:int
# 返回3门科目中最高的分数: get_course() 返回类型:int
# 写好类以后，可以定义2个同学测试下:
# xm = Student('xiaoming', 20, [69,88,100])
# xm.get_name() 返回 xiaoming
# xm.get_age() 返回 20
# xm.course() 返回 100
#
# class Student():
#     def __init__(self,name,age,course):
#         self.name = name
#         self.age = age
#         self.course = course
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def get_course(self):
#         return max(self.course)
#
#
# xm = Student('xiaoming',20,[69,88,100])
# print(xm.get_name()) #返回 xiaoming
# print(xm.get_age()) #返回 20
# print(xm.get_course()) #返回 100
#



# 2.定义一个列表的操作类：ListInfo
# 实例方法为:
# - 列表元素添加: add_value(valuename) [valuename:字符串或整数类型]
# - 列表元素取值：get_value(valuename) [valuename:字符串或整数类型]
# - 列表合并：update_list(list) [list:列表类型]

# class ListInfo:
#
#     def __init__(self, lst):
#
#         self.lst = lst
#
#     def add_value(self, valuename):
#
#         self.lst.append(valuename)
#
#         print(self.lst)
#
#     def get_value(self, valuename):
#
#         print(self.lst[valuename])
#
#     def update_list(self, list1):
#
#         print(self.lst + list1)
#
#
# a = ListInfo([1, 2, 3])
#
# a.add_value(4)
#
# a.get_value(2)
#
# a.update_list([5, 6, 5])



#
# 3.看代码猜结果,并画出对应的空间图
# a.
#
# class A:
#     Country = '中国'
#     def __init__(self, name, age, country):
#         self.name = name
#         self.age = age
#
#     def func1(self):
#         print(self)
#
# a = A('alex', 83, '印度')
# b = A('wusir', 74, '泰国')
# A.Country = '英国'
# a.Country = '日本'
# print(a.Country) # 日本
# print(b.Country) # 英国
# print(A.Country) # 英国
# # b.
#
# class A:
#     Country = '中国'
#     def __init__(self, name, age, country):
#         self.name = name
#         self.age = age
#         self.Country = country
#
#     def func1(self):
#         print(self)
#
# a = A('alex', 83, '印度')
# b = A('wusir', 74, '泰国')
# A.Country = '英国'
# a.Country = '日本'
# print(a.Country) # 日本
# print(b.Country) # 泰国
# print(A.Country) # 英国
# c.
#
# class A:
#     Country = '中国'
#     def __init__(self, name, age, country):
#         self.name = name
#         self.age = age
#
#     def Country(self):
#         return self.Country
#
# a = A('alex', 83, '印度')
# b = A('wusir', 74, '泰国')
# print(a.Country)  # 内存地址
# print(a.Country()) # 内存地址