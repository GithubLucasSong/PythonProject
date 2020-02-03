# 4，定义一个列表的操作类：Listinfo
# 包括的方法:
# 1
# 列表元素添加: add_key(keyname)[keyname:字符串或者整数类型]
# 2
# 列表元素取值：get_key(num)[num:整数类型]
# 3
# 列表合并：update_list(list)[list:列表类型]
# 4
# 删除并且返回最后一个元素：del_key()
# list_info = Listinfo([44, 222, 111, 333, 454, 'sss', '333'])


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
