import sys

input_s = sys.stdin.readline

class answer:
    
    def __init__(self, *args, **kwargs):
        self.n = int(input_s())
        self.graph = [[] for _ in range(self.n + 1)]
        self.visit = [False for _ in range(self.n + 1)]

    def add_edge(self):
        self.edges = int(input_s())

        for _ in range(self.edges):
            u, v = map(int, input_s().split())
            self.graph[u].append(v)
            self.graph[v].append(u)

    def dfs(self, v):        
        self.visit[v] = True
        count = 1

        for vis_node in self.graph[v]:
            if not self.visit[vis_node]:
                count += self.dfs(vis_node)

        return count


ans = answer()
ans.add_edge()
print(ans.dfs(1)-1)