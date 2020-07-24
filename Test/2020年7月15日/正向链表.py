





class Node():
    def __init__(self, item):
        self.item = item
        self.next = None


class Link():
    def __init__(self):
        self.head = Node('头')
        self.prev_node = self.head

    def add(self, item):
        node = Node(item)
        self.prev_node.next = node
        self.prev_node = node


link = Link()
link.add(3)
link.add(6)
link.add(9)

print(link.head.item)
print(link.head.next.item)
print(link.head.next.next.item)
print(link.head.next.next.next.item)
