# 9，建立一个汽车类Auto，包括轮胎个数，汽车颜色，车身重量，速度等属性
# 至少要求汽车能够加速
# 减速
# 停车
# 再定义一个小汽车类CarAuto
# 继承Auto
# 并添加空调、CD属性，并且重新实现方法覆盖加速、减速的方法

class Auto():

    def __init__(self,wheel,color,weight,speed):
        self.wheel = wheel
        self.color = color
        self.weight = weight
        self.speed = speed

    def speed_up(self):
        print('加速')

    def speed_down(self):
        print('减速')

    def parking(self):
        print('停车')

class CarAuto(Auto):
    def __init__(self, wheel, color, weight, speed,air,cd):
        super().__init__(wheel, color, weight, speed)
        self.air = air
        self.cd = cd

    def speed_up(self):
        print('新加速')

    def speed_down(self):
        print('新减速')

car = CarAuto(4,'red',1000,120,4,1)
print(car.color)
car.speed_up()
