import sys
sys.setrecursionlimit(10**6)

input_s = sys.stdin.readline

class anser:

    def __init__(self, *args, **kwargs):
        self.v, self.e = map(int, input_s().split())
        self.graph = []
        self.parent = [x for x in range(self.v + 1)]

    def add_edge(self):
         for _ in range(self.e):
            u, v, weight = map(int, input().split())
            self.graph.append((weight, u, v))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u < v:
            self.parent[v] = u
        else:
            self.parent[u] = v

    def kruskalMSTw(self):
        self.graph.sort()
        mst_cost = 0
        mst_edges = 0

        for weight, u, v in self.graph:
            if self.find(u) != self.find(v):
                self.union(u, v)
                mst_cost += weight
                mst_edges += 1
                if mst_edges == self.v - 1:
                    break

        return mst_cost

ans = anser()
ans.add_edge()

print(ans.kruskalMSTw())