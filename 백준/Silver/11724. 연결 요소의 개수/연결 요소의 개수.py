import sys
sys.setrecursionlimit(10**6)

def dfs(graph, v, visited):
    visited[v] = True
    # print(v, end=' ')

    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

n, e = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n+1)]

for i in range(e):
    u, v = list(map(int, sys.stdin.readline().split()))
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in graph]
component_count=0

for node in range(1, n+1):
    if not visited[node]:
        dfs(graph, node, visited)
        component_count += 1

print(component_count)