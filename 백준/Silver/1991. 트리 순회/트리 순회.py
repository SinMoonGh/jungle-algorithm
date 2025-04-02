import sys

input_s = sys.stdin.readline

class answer:
    
    def __init__(self, *args, **kwargs):
        self.n = int(input_s())
        self.graph = {}
        self.pro_visit = {}
        self.ino_visit = {}
        self.pto_visit = {}

    def add_edge(self):
        for _ in range(self.n):
            root, left, right = map(str, input_s().split())
            self.graph[root] = [left, right]
            self.pro_visit[root] = False
            self.ino_visit[root] = False
            self.pto_visit[root] = False

    def preorder(self, node):
        if node == '.' or self.pro_visit[node]:
            return
        
        self.pro_visit[node] = True
        print(node, end='')
        left_ch, right_ch = self.graph[node]        

        self.preorder(left_ch)
        self.preorder(right_ch)

    def inorder(self, node):
        if node == '.' or self.ino_visit[node]:
            return
        
        self.ino_visit[node] = True
        left_ch, right_ch = self.graph[node]        

        self.inorder(left_ch)
        print(node, end='')
        self.inorder(right_ch)

    def postorder(self, node):
        if node == '.' or self.pto_visit[node]:
            return
        
        self.pto_visit[node] = True
        left_ch, right_ch = self.graph[node]        

        self.postorder(left_ch)
        self.postorder(right_ch)
        print(node, end='')




ans = answer()
ans.add_edge()

ans.preorder('A')
print()
ans.inorder('A')
print()
ans.postorder('A')
    