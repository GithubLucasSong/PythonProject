#
#
# class Elephant():
#     def __init__(self,name):
#         self.name = name
#
#     def open(self,obj):
#         obj.open_door()
#
#     def close(self,obj):
#         obj.close_door()
#
#
# class Haier():
#     def open_door(self):
#         print('冰箱门被打开了')
#
#     def close_door(self):
#         print('冰箱门被关上了')
#
#
# class Medi():
#     def open_door(self):
#         print('冰箱门被打开了')
#
#     def close_door(self):
#         print('冰箱门被关上了')
#
# m = Medi()
# f = Elephant('小飞象')
# f.open(m)
# f.close(m)


#模拟CS游戏

class Person():
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp

    def knife(self,obj):
        obj.hp -= 10
        print(f'{self.name}划了{obj.name}一刀，{obj.name}掉了10滴血！')

    def fire(self,ak,obj):
        ak.fire(self,obj)



class Police(Person):
    call = '警察'
    def __init__(self,name,hp,job):
        self.job = job
        super().__init__(name,hp)



class Bandit(Person):
    call = '土匪'
    def __init__(self,name,hp,job):
        self.job = job
        super().__init__(name, hp)


class AK():
    def __init__(self):
        self.ak = 90

    def fire(self,obj,obj1):
        print(f'{obj.name}使用AK打了一下{obj1.name}，{obj1.name}掉了90滴血')


p1 = Police('海报',100,'警察')
ak1 = AK() #创建一把枪
b1 = Bandit('座山雕',100,'土匪')
ak1.fire(p1,b1)
p1.fire(ak1,b1) # 人拿着枪要开枪


