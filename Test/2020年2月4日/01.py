# class Person:
#     def __init__(self,name,age,weight,height):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.height = height
#         self.__score = 70
#     #将某个方法伪装成属性，这个方法需要有返回值
#     # @property
#     # def bmi(self):
#     #     return self.weight/(self.height*self.height)
#     #属性一般有三种访问方式：获取，修改，删除
#
#     #当对象.score 被放在print中的时候，会自动调用property下面那个方法
#     @property
#     def score(self):
#         return self.__score + 30
#     #一定先有取值的方法，才能写设置值或者删除值的方法
#     #在@后面写刚才取值的那个方法的方法名，后面写。setter
#     #接下来，定义一个方法，方法名也要和取值的方法同名
#     #这个方法需要接收一个参数，用来给私有属性赋值
#     #如果是赋值操作，自动调用setter后面的方法
#     @score.setter
#     def score(self,sc):
#         if sc < 0:
#             print("输入有误")
#         else:
#             self.__score = sc
#     @score.deleter
#     def score(self):
#         del self.__score
# #总结，如果一个私有属性加上了property，那么他当前就变为可读的
# #再加上setter之后，他就变成了可读可写
# p1 = Person("shang",32,80,1.9)
# print(p1.score)
# p1.score = 123
# print(p1.score)
# #当通过。去访问这个伪装过的属性时，可以获取到方法的返回值
# # print(p1.bmi)
# # bmi = p1.bmi()
# # print(bmi)

import time

class P():
    def __init__(self):
        self.__score = 60

    @property
    def score(self):
        return self.__score + 30

    @score.setter
    def score(self,new_score):
        self.__score = new_score

    @score.deleter
    def score(self):
        del self.__score
        print('已删除')
p = P()
print(p.score)
p.score = 70
print(p.score)
time.sleep(1)
del p.score
