# 五
# 编程题
#
# 1.
# 简述面向对象中为什么要有继承? 将不同类的相同属性和方法做封装 减少代码量
#
# 2.
# Python继承时，查找成员的顺序遵循什么规则? 子类中有使用子类的 子类中没有使用父类的
#
# 3.
# 需求：
#
# 房子有户型，总面积（私有）和家具名称列表
# 新房子没有任何的家具
#
# 家具有名字和占地面积，其中
# 床：占4平米
#
# 衣柜：占2平面
#
# 餐桌：占1
# .5
# 平米
#
# 将以上三件家具添加到房子中
# 打印房子时，要求输出: 户型，总面积，剩余面积，家具名称列表
#

class House():
    def __init__(self,house_type,area,furniture_list=[]):
        self.house_type = house_type
        self.__area = area
        self.surplus = area
        self.furniture_list = furniture_list

    def add_furniture(self,name,size):
        self.furniture_list.append(name)
        self.surplus -= size

    @property
    def house(self):
        return f'户型:{self.house_type},总面积:{self.__area},剩余面积:{self.surplus},家具列表{self.furniture_list}'

h = House('三室两厅',100)
print(h.house)
h.add_furniture('床',4)
h.add_furniture('衣柜',2)
h.add_furniture('餐桌',1.5)
print(h.house)
