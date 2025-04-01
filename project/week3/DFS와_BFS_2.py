import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    dq = deque()

    visited[v] = True
    dq.append(v)

    while len(dq)>0:
        p_dt = dq.popleft()
        print(p_dt, end=' ')

        for i in sorted(graph[p_dt]):
            if not visited[i]:
                visited[i] = True
                dq.append(i)

def main():
    n, edges, st = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    dfs_visited = [False for _ in range(n+1)]
    bfs_visited = [False for _ in range(n+1)]

    for _ in range(edges):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)


    dfs(graph, st, dfs_visited)
    print()
    bfs(graph, st, bfs_visited)


main()