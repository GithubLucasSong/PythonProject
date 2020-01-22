class Person():
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp

    def knife(self,obj):
        obj.hp -= 10
        print(f'{self.name}划了{obj.name}一刀，{obj.name}掉了10滴血！')

    def fire(self,obj):
        self.ak1.fire(self,obj)


class Police(Person):
    call = '警察'
    def __init__(self,name,hp,job,ak1):
        self.job = job
        self.ak1 = ak1 #组合
        super().__init__(name,hp)



class Bandit(Person):
    call = '土匪'
    def __init__(self,name,hp,job,ak1):
        self.job = job
        self.ak1 = ak1
        super().__init__(name, hp)


class AK():
    def __init__(self):
        self.ak = 90

    def fire(self,obj,obj1):
        print(f'{obj.name}使用AK打了一下{obj1.name}，{obj1.name}掉了90滴血')

# 1.实例化一个枪对象
ak1 = AK()
# 2.实例化一个警察对象
p1 = Police('孤狼',100,'特种兵',ak1)
# 3.实例化一个土匪对象
b1 = Bandit('黑猫',100,'雇佣兵',ak1)

p1.fire(b1)
b1.fire(p1)
