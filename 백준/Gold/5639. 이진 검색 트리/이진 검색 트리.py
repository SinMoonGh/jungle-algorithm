import sys
sys.setrecursionlimit(10**6)

input_s = sys.stdin.readline

class Node:
    
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    

class BinarySearchTree:
    
    def __init__(self):
        self.root = None

    def search(self, key):
        p = self.root

        while True:
            if p == None:
                return None
            
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            elif key > p.key:
                p =  p.right

    def add_node(self, key, value = None):
        if self.root is None:
            self.root = Node(key, value)
            return
        
        node = self.root

        while True:
            if key == node.key:
                return True
            elif key < node.key:
                if node.left == None:
                    node.left = Node(key, value)
                    return
                else:
                    node = node.left
            elif key > node.key:
                if node.right == None:
                    node.right = Node(key, value)
                    return
                else:
                    node = node.right

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key)

bst = BinarySearchTree()

node_list = sys.stdin.read().splitlines()
values = list(map(int, node_list))

for i in values:
    bst.add_node(key=i)

bst.postorder(bst.root)