# 1 --- 2
# |     |
# 4 --- 3

# 간선 목록 :
# 1,2
# 1,4
# 2,3
# 3,4

matrix = [[0 for _ in range(4)] for _ in range(4)]
# matrix[1][2] = 1
# matrix[1][2] = 1

# matrix[1][4] = 1
# matrix[4][1] = 1

# matrix[2][3] = 1
# matrix[3][2] = 1

# matrix[3][4] = 1
# matrix[4][3] = 1

print(matrix)

graph = {
  1: [],
  2: [],
  3: [],
  4: []
}

graph[1] = 2
graph[2] = 1
print(graph)