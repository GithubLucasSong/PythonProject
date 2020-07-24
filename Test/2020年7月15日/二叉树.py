# 封装节点
class Node():
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class Tree():
    def __init__(self):  # 构建一个空树
        self.root = None

    def addNode(self, item):
        node = Node(item)
        # 如果树为空
        if self.root == None:
            self.root = node
            return
        # 树为非空
        cur = self.root
        q_list = [cur]

        while True:
            first_item = q_list.pop(0)
            if first_item.left != None:  # 判断取出节点的左节点是否为空，不为空加入到列表
                q_list.append(first_item.left)
            else:
                first_item.left = node
                break
            # 判断右叶子节点是否为空
            if first_item.right != None:
                q_list.append(first_item.right)
            else:
                first_item.right = node
                break

    def travel(self):
        cur = self.root
        q_list = [cur]
        while q_list:
            first_item = q_list.pop(0)
            print(first_item.item)
            if first_item.left != None:
                q_list.append(first_item.left)
            if first_item.right != None:
                q_list.append(first_item.right)

    def forward(self, root):  # 将根左右作用在每一颗子树中，子树和子树是基于什么区分
        # 设计一个结束递归的条件
        if root == None:
            return
        # 参数root是子树的根节点
        print(root.item)
        self.forward(root.left)
        self.forward(root.right)

    def middle(self, root):
        if root == None:
            return
        self.middle(root.left)
        print(root.item)
        self.middle(root.right)
    def back(self,root):
        if root == None:
            return
        self.back(root.left)
        self.back(root.right)
        print(root.item)


tree = Tree()
tree.addNode(1)
tree.addNode(2)
tree.addNode(3)
tree.addNode(4)
tree.addNode(5)
tree.addNode(6)
tree.travel()
print('-------------')
tree.forward(tree.root)
print('-------------')
tree.middle(tree.root)
print('-------------')
tree.back(tree.root)
