graph = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [],
    5: []
}

from collections import deque

def bfs(graph, start):
    visited = {v: False for v in graph}
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

bfs(graph, 1)