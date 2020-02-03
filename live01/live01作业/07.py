# 7，士兵类（Soldier）具有名字，和枪支（gun）两个属性
# 枪支属性默认为None值
# 士兵可以使用枪支开火(fire)，如果没有获得枪则提示“还没有枪”
# 枪类（Gun）有型号(model)
# 和子弹数量（bullet_count）属性
# 枪能够发射子弹(shoot)，也可以装填子弹(add_bullet)，如果子弹数为0则不能继续发射

import time

class Soldier():

    def __init__(self,name,gun=None):
        self.name = name
        self.gun = gun

    def fire(self):
        if self.gun == None:
            print('还没有枪')
        else:
            while True:
                if self.gun.shoot(self.name) == False:
                    self.gun.add_buttle(self.name)
                else:
                    time.sleep(0.3)



class Gun(Soldier):
    def __init__(self,model,bullet_count):
        self.model = model
        self.bullet_count = bullet_count

    def shoot(self,name):
        if self.bullet_count > 0:
            self.bullet_count -= 1
            print(f'{name}使用{self.model}开火,剩余{self.bullet_count}子弹')

        else:
            print(f'{self.model}没有子弹了')
            return False

    def add_buttle(self,name):
        self.bullet_count += 30
        time.sleep(3)
        print(f'{name}给{self.model}装填子弹,剩余{self.bullet_count}子弹')

gun = Gun('AK47',30)
person = Soldier('肥皂',gun)
person.fire()
