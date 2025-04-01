# 시작 노드를 방문한다.

# 인접한 노드 중 아직 방문하지 않은 노드가 있으면 그 노드를 방문한다.

# 방문한 노드에서 다시 위의 과정을 반복한다.

# 더 이상 방문할 수 있는 노드가 없다면, 이전 노드로 되돌아간다 (백트래킹).

# 모든 노드를 방문할 때까지 이 과정을 반복한다.

graph = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [],
    5: []
}

visited = {i: False for i in graph}

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

print(visited)
dfs(graph, 1, visited)
