# 节点的封装
class Node():
    def __init__(self, item):
        self.item = item  # 向节点中添加的数据值
        self.next = None  # next是用来指向链表中下一个节点


# 链表的封装
class Link():
    def __init__(self):  # 构造出一个空链表
        # _head使用来指向链表中第一个节点
        self._head = None

    # 向链表的头部插入节点
    def add(self, item):
        # 实例化一个节点对象
        node = Node(item)
        node.next = self._head
        self._head = node

    def travel(self):  # 遍历每一个节点
        #         print(self._head.item)
        #         print(self._head.next.item)
        #         print(self._head.next.next.item)
        cur = self._head
        while cur:
            print(cur.item)
            cur = cur.next

    def length(self):  # 返回链表中节点的个数
        count = 0
        cur = self._head
        while cur:
            count += 1
            cur = cur.next
        return count

    def is_empty(self):
        return self._head == None

    def search(self, item):  # 在链表中查找是否存在item对应的节点
        cur = self._head
        find = False
        while cur:
            if cur.item == item:
                find = True
                break
            else:
                cur = cur.next
        return find

    def append(self, item):  # 像链表的尾部插入节点
        node = Node(item)
        if self._head == None:  # 链表为空
            self._head = node
            return
        # 链表为非空的情况
        cur = self._head
        pre = None  # pre指向的是cur前面的一个节点
        while cur:
            pre = cur
            cur = cur.next
        pre.next = node

    def insert(self, pos, item):  # 要向链表中指定的位置插入新的节点
        node = Node(item)
        if pos == 0:
            node.next = self._head
            self._head = node
            return
        pre = None
        cur = self._head
        for i in range(pos):
            pre = cur
            cur = cur.next
        pre.next = node
        node.next = cur

    def remove_index(self, pos):  # 根据下标删除
        cur = self._head
        pre = None
        if pos == 0:
            self._head = cur.next
            return
        for i in range(pos):
            pre = cur
            cur = cur.next
        pre.next = cur.next

    def remove_item1(self, item):  # 根据item删除方法1
        cur = self._head
        pre = None
        # 如果删除的是第一个节点
        if cur.item == item:
            self._head = cur.next
            return
        while cur:
            pre = cur
            cur = cur.next
            if cur == None:  # 如果为None代表链表循环到尾部
                print('没有这个节点')
                return
            if cur.item == item:
                pre.next = cur.next
                break

    def remove_item2(self, item):  # 根据item删除方法2
        cur = self._head
        pre = None

        # 如果删除的是第一个节点
        if cur.item == item:
            self._head = cur.next
            return

        # 删除的是非第一个节点的做法
        while True:
            pre = cur
            cur = cur.next
            if cur.item == item:  # cur就是我们想要删除的节点，pre就是删除节点的前一个节点
                pre.next = cur.next
                break
            if cur == None:
                break

    def reverse(self):  # 将链表的节点进行倒置
        pre = self._head
        cur = pre.next
        next_node = cur.next

        pre.next = None

        while cur:
            cur.next = pre
            pre = cur
            cur = next_node
            if cur:
                next_node = next_node.next
        self._head = pre


link = Link()
link.add(3)
link.add(6)
link.add(9)
link.add(12)
# link.append(15)
# link.insert(0, 10)
# link.remove_index(1)
# link.remove_item2(6)
link.reverse()
link.travel()
# print(link.length())
# print(link.is_empty())
# print(link.search(6))

# print(link._head.next.item)
# print(link._head.next.next.item)
