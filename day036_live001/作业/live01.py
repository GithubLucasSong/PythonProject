1，定义一个圆形类, 半径是这个圆形的属性, 实例化一个半径为5的圆形, 一个半径为10的圆形
完成方法
计算圆形面积
计算圆形周长
import math

class Round():
    def __init__(self,r):
        self.r = r

    def get_area(self):
        print(f'面积为{math.pi*(self.r**2)}')

    def get_perimeter(self):
        print(f'周长为{2*math.pi*self.r}')

round5 = Round(5)
round10 = Round(10)
round5.get_area()
round5.get_perimeter()



2，定义一个用户类, 用户名和密码是这个类的属性, 实例化两个用户, 分别有不同的用户名和密码
登陆成功之后才创建用户对象
设计一个方法
修改密码

class User():
    user_dic = {'alex': '123', 'blex': '456'}

    def __init__(self,unm,pwd):
        self.unm = unm
        self.pwd = pwd

    def login(self):

    def set_pwd(self,newpwd):
        self.pwd = newpwd
        User.user_dic[self.unm] = self.pwd





3，定义一个学生类。有下面的类属性：
1
姓名
2
年龄
3
成绩（语文，数学，英语)[每课成绩的类型为整数]
类方法：
1
获取学生的姓名：get_name()
返回类型: str
2
获取学生的年龄：get_age()
返回类型: int
3
返回3门科目中最高的分数。get_course()
返回类型: int
写好类以后，可以定义2个同学测试下:
zm = Student('zhangming', 20, [69, 88, 100])
返回结果：
zhangming
20
100

class Student():
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.course)


xm = Student('xiaoming',20,[69,88,100])
print(xm.get_name()) #返回 xiaoming
print(xm.get_age()) #返回 20
print(xm.get_course()) #返回 100


4，定义一个列表的操作类：Listinfo
包括的方法:
1
列表元素添加: add_key(keyname)[keyname:字符串或者整数类型]
2
列表元素取值：get_key(num)[num:整数类型]
3
列表合并：update_list(list)[list:列表类型]
4
删除并且返回最后一个元素：del_key()
list_info = Listinfo([44, 222, 111, 333, 454, 'sss', '333'])


class ListInfo:

    def __init__(self, lst):

        self.lst = lst

    def add_value(self, valuename):

        self.lst.append(valuename)

        print(self.lst)

    def get_value(self, valuename):

        print(self.lst[valuename])

    def update_list(self, list1):

        print(self.lst + list1)

    def del_key(self):
        print(self.lst)
        return self.lst.pop()


a = ListInfo([44, 222, 111, 333, 454, 'sss', '333'])

a.add_value(4)

a.get_value(2)

a.update_list([5, 6, 5])

print(a.del_key())


5，英雄自残
一秒打自己一次
掉的血是一个波动值，可以随机选择多个技能
有一定闪避概率，没血了会死

6，命名空间四件套
读程序, 标出程序的执行过程, 画出内存图解, 说明答案和为什么
请不要想当然, 执行之后检查结果然后再确认和自己的猜想是不是一致
(1)


class A:
    Country = '中国'  # 静态变量/静态属性 存储在类的命名空间里的

    def __init__(self, name, age, country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age

    def func1(self):
        print(self)


a = A('alex', 83, '印度')
b = A('wusir', 74, '泰国')
A.Country = '英国'
a.Country = '日本'
print(a.Country)
print(b.Country)
print(A.Country)

(2)


class A:
    Country = ['中国']  # 静态变量/静态属性 存储在类的命名空间里的

    def __init__(self, name, age, country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age

    def func1(self):
        print(self)


a = A('alex', 83, '印度')
b = A('wusir', 74, '泰国')
a.Country[0] = '日本'
print(a.Country)
print(b.Country)
print(A.Country)

(3)


class A:
    Country = '中国'  # 静态变量/静态属性 存储在类的命名空间里的

    def __init__(self, name, age, country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
        self.Country = country

    def func1(self):
        print(self)


a = A('alex', 83, '印度')
b = A('wusir', 74, '泰国')
A.Country = '英国'
a.Country = '日本'
print(a.Country)
print(b.Country)
print(A.Country)

(4)


class A:
    Country = '中国'  # 静态变量/静态属性 存储在类的命名空间里的

    def __init__(self, name, age, country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age

    def Country(self):
        return self.Country


a = A('alex', 83, '印度')
b = A('wusir', 74, '泰国')
print(a.Country)
print(a.Country())

7，士兵类（Soldier）具有名字，和枪支（gun）两个属性
枪支属性默认为None值
士兵可以使用枪支开火(fire)，如果没有获得枪则提示“还没有枪”
枪类（Gun）有型号(model)
和子弹数量（bullet_count）属性
枪能够发射子弹(shoot)，也可以装填子弹(add_bullet)，如果子弹数为0则不能继续发射

8，定义宠物类（ Pet ），猫类（Cat）和狗类（Dog）
宠物都有属性姓名（name）和年龄(age)
宠物都有吃（eat）、喝（drink）、叫（shout）的方法
猫除了具有宠物类的方法，还有爬树（ climbTree ）的方法
狗除了具有宠物类的方法，还有警戒（ police）的方法

9，建立一个汽车类Auto，包括轮胎个数，汽车颜色，车身重量，速度等属性
至少要求汽车能够加速
减速
停车
再定义一个小汽车类CarAuto
继承Auto
并添加空调、CD属性，并且重新实现方法覆盖加速、减速的方法

10，银行卡类（BankCard）有余额（balance）属性和存款（deposit）取款（draw）的方法，
只要取款金额小于余额即可完成取款操作
信用卡类（CreditCard）继承自银行卡类，信用卡多了透支额度（overdraft）属性，
# 如果卡中余额和透支额度的和大于取款金额即可完成取款。如果透支，显示透支金额