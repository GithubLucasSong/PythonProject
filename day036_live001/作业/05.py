# 5，英雄自残
# 一秒打自己一次
# 掉的血是一个波动值，可以随机选择多个技能
# 有一定闪避概率，没血了会死


import random
import time

class Hero():

    def __init__(self,name,hp,ce):
        self.name = name
        self.hp = hp
        self.ce = ce


    def attack_self(self):
        if self.hp > 0:
            if self.is_miss():
                print('闪避')
            else:
                self.hp -= self.ce_fluctuate()
                if self.hp < 0:
                    self.hp = 0
                print('{}攻击了自己，剩余{:.0f}血'.format(self.name,self.hp))
        else:
            print(f'{self.name}死了')
            return False





    def is_miss(self):
        if random.random() < 0.1:
            return True
        else:
            return False

    def ce_fluctuate(self):
        return self.ce * random.uniform(0.5,1.5)

    def attack_self_forever(self):
        while True:
            if self.attack_self() == False:
                break
            time.sleep(1)

hero = Hero('盖伦',200,30)
hero.attack_self_forever()


