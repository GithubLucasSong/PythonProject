class Node():
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None


class SortTree():
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root == None:  # 树为空
            self.root = node
            return
        # 树为非空
        cur = self.root
        while True:
            if cur.item < item:  # 插入节点的值大于根节点，将节点插入到根节点右侧
                if cur.right == None:
                    cur.right = node
                    break
                else:
                    cur = cur.right
            else:  # 将节点插入到根节点的左侧
                if cur.left == None:
                    cur.left = node
                    break
                else:
                    cur = cur.left

    def middle(self, root):
        if root == None:
            return
        self.middle(root.left)
        print(root.item)
        self.middle(root.right)


tree = SortTree()
alist = [3,8,5,7,6,2,1]
for i in alist:
    tree.add(i)
tree.middle(tree.root)