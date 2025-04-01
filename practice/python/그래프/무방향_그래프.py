# 1 --- 2
# |     |
# 4 --- 3

import sys

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 무방향 그래프 구현
n, e = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n+1)]

for i in range(e):
    u, v = list(map(int, sys.stdin.readline().split()))
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in graph]

dfs(graph, 1, visited)