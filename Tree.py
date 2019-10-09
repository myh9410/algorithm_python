class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if node.left is None:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def pre_order_traversal(self):
        if self.root is not None:
            self._pre_order_traversal(self.root)

    def _pre_order_traversal(self, node):
        if node == None: return
        print(node.data)
        self._pre_order_traversal(node.left)
        self._pre_order_traversal(node.right)


bst = BST()
N = int(input())
for i in range(N):
    s= input()
    bst.insert(list(s))

bst.pre_order_traversal()