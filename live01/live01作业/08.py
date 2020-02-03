# 8，定义宠物类（ Pet ），猫类（Cat）和狗类（Dog）
# 宠物都有属性姓名（name）和年龄(age)
# 宠物都有吃（eat）、喝（drink）、叫（shout）的方法
# 猫除了具有宠物类的方法，还有爬树（ climbTree ）的方法
# 狗除了具有宠物类的方法，还有警戒（ police）的方法

class Pet():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        pass

    def drink(self):
        pass

    def shout(self):
        pass


class Cat(Pet):
    def __init__(self,name,age):
        super().__init__()

    def climbTree(self):
        pass


class Dog():
    def __init__(self,name,age):
        super().__init__()

    def police(self):
        pass
