import sys
from collections import deque
sys.setrecursionlimit(10**6)

def dfs(graph, v, visited, parent):
    visited[v] = True
    print(v, end=' ')
    
    for u in sorted(graph[v]):
        if visited[u] == True and u != parent:
            return True
        elif not visited[u]:
            dfs(graph, u, visited, v)


def bfs(graph, v, visited):
    dq = deque()
    visited[v] = True
    dq.append(v)

    while len(dq) > 0:
        pop_data = dq.popleft()
        print(pop_data, end=' ')
 
        for u in sorted(graph[pop_data]):
            if not visited[u]:
                dq.append(u)
                visited[u] = True

n, m, st = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = list(map(int, sys.stdin.readline().split()))
    graph[u].append(v)
    graph[v].append(u)

dfs_visited = [False for _ in graph]
bfs_visited = [False for _ in graph]

for i in range(st, n+1):
    # cicle이 발생하면 즉시 종료
    if dfs(graph, i, dfs_visited, None):
        break

print()
for i in range(st, n+1):
    # cicle이 발생하면 즉시 종료
    if not bfs_visited[i]:
        if bfs(graph, i, bfs_visited):
            break
