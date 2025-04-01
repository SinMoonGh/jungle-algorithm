import sys
from collections import deque

class answer:
    def __init__(self):
        self.n, self.m = map(int, sys.stdin.readline().split())
        self.graph = None
        self.in_degree = None
        self.queue = deque()
    
    def build_graph(self):        
        self.graph = [[] for _ in range(self.n + 1)]
        self.in_degree = [0] * (self.n + 1)

        # print(self.graph)

    def add_edge(self):
        for _ in range(self.m):
            a, b = map(int, sys.stdin.readline().split())
            self.graph[a].append(b) 
            self.in_degree[b] += 1

        # print(self.in_degree)

    def init_queue(self):
        for i in range(1, self.n + 1):
            if self.in_degree[i] == 0:
                self.queue.append(i) 

        # print(self.queue)

    def topological_sort(self):
        while len(self.queue) > 0:
            pop_dt = self.queue.popleft()
            print(pop_dt, end=' ')

            for next_node in self.graph[pop_dt]:
                self.in_degree[next_node] -= 1

                if self.in_degree[next_node] == 0:
                    self.queue.append(next_node)

ans = answer()
ans.build_graph()
ans.add_edge()
ans.init_queue()
ans.topological_sort()