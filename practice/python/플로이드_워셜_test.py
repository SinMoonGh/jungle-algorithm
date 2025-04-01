N = 3
INF = 1e9
D = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    D[i][i] = 0

# 간선 정보 입력
D[1][2] = 4
D[2][3] = 2
D[1][3] = 10

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])
        print(f'출발 지점 : {i}, 경유 지점 : {k}, 도착 지점 : {j}')

print(D[1][3])

D = [[INF] * (N + 1) for _ in range(N + 1)]

# 간선 정보 입력
D[1][2] = 4
D[2][3] = 2
D[1][3] = 10

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            old = D[i][j]
            via = D[i][k] + D[k][j]
            D[i][j] = min(D[i][j], via)

            print(f"[i={i}, j={j}, k={k}] 기존: {old}, 경유경로: {D[i][k]} + {D[k][j]} = {via} → 갱신결과: {D[i][j]}")

print(D[1][3])