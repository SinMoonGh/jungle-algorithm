import sys, heapq

INF = float("inf")

class answer:
    def __init__(self):
        self.n = int(sys.stdin.readline())
        self.m = int(sys.stdin.readline())
        self.pq = []


    def build_graph(self):        
        self.graph = [[] for _ in range(self.n + 1)]
        self.distance = [INF for _ in range(self.n + 1)]


    def add_edge(self):
        for _ in range(self.m):
            u, v, cost = map(int, sys.stdin.readline().split())
            self.graph[u].append([cost, v])


    def init_pq(self):
        self.start, self.end = map(int, sys.stdin.readline().split())
        self.distance[self.start] = 0

        heapq.heappush(self.pq, [0, self.start]) 


    def dijkstra(self):
        while len(self.pq) > 0:
            pop_dt = heapq.heappop(self.pq)
            current = pop_dt[1]
            cur_dist = pop_dt[0]

            if self.distance[current] < cur_dist:
                continue

            for i in self.graph[current]:
                edge_cost = i[0]
                next_node = i[1]

                new_dist = cur_dist + edge_cost
                if self.distance[next_node] > new_dist:
                    self.distance[next_node] = new_dist
                    heapq.heappush(self.pq, [new_dist, next_node])

        print(self.distance[self.end])

ans = answer()
ans.build_graph()
ans.add_edge()
ans.init_pq()
ans.dijkstra()