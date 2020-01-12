# a,b = 1,2
# print(a,b)

# a,b = ('你好','世界')
# print(a,b)
#
#
# a,b = ['你好','大飞哥']
# print(a,b)
#

# a,b = {'汪峰':'北京北京','王菲':'天后'}
# print(a,b)

# s1 = {"刘能", "赵四", "⽪⻓⼭"}
# s2 = {"刘科⻓", "冯乡⻓", "⽪⻓⼭"}
# # 交集
# # 两个集合中的共有元素
# print(s1 & s2) # {'⽪⻓⼭'}

# lst = [1,2,3,[6,7,8]]
# lst2 = lst[:]
# lst.append(9)
# print(lst2)

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
# # #检测是否含有某属性
# # print(hasattr(obj,'name'))
# # print(hasattr(obj,'say_hi'))
#
# #获取属性
# n=getattr(obj,'name')
# print(n)
# func=getattr(obj,'say_hi')
# func()
#
# print(getattr(obj,'aaaaaaaa','不存在啊')) #报错

# #设置属性
# setattr(obj,'sb',True)
# setattr(obj,'show_name',lambda self:self.name+'sb')
# print(obj.__dict__)
# print(obj.show_name(obj))
#
# #删除属性
# delattr(obj,'age')
# delattr(obj,'show_name')
# delattr(obj,'show_name111')#不存在,则报错
#
# print(obj.__dict__)
#
# 对实例化对象的示例

# def eat(*args):
#
#     print('我想吃',args)
#
# eat('大米饭','中米饭','小米饭')  # 收到的结果是一个tuple元祖

# def warning():
#     print('警告')
# s = input(':')
# exec(s)

# print(hash(12345))
print(pow(2,64))