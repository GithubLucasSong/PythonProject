# 1，定义一个圆形类, 半径是这个圆形的属性, 实例化一个半径为5的圆形, 一个半径为10的圆形
# 完成方法
# 计算圆形面积
# 计算圆形周长
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
