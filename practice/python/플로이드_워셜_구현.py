import sys

INF = float('inf')

class answer:
    
    def __init__(self, *args, **kwargs):
        self.n = int(sys.stdin.readline())
        self.m = int(sys.stdin.readline())        

    def build_graph(self):
        self.graph = [[INF]*(self.n + 1) for _ in range(self.n + 1)]
        for i in range(1, self.n + 1):
            self.graph[i][i] = 0

    def add_edge(self):
        for _ in range(self.m):
            a, b, c = map(int, sys.stdin.readline().split())
            self.graph[a][b] = c

    def floyd_warshall(self):
        start, end = map(int, sys.stdin.readline().split())

        for k in range(1, self.n + 1):
            for i in range(1, self.n + 1):
                for j in range(1, self.n + 1):
                    self.graph[i][j] = min(self.graph[i][j], self.graph[i][k] + self.graph[k][j])

        return self.graph[start][end]

    
ans = answer()
ans.build_graph()
ans.add_edge()

print(ans.floyd_warshall())