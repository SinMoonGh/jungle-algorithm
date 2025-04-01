import sys

sys.stdin = open('project/week2/input.txt', "r")

def recur(arr, r, c, n):
    sum_dt = 0

    for i in range(r, r+n):
        for j in range(c, c+n):
            sum_dt += arr[i][j]

    if sum_dt == (n*n):
        return (0, 1)
    elif sum_dt == 0:
        return (1, 0)
    else:
        w1, b1 = recur(arr, r, c, n//2)
        w2, b2 = recur(arr, r, c + n//2, n//2)
        w3, b3 = recur(arr, r + n//2, c, n//2)
        w4, b4 = recur(arr, r + n//2, c + n//2, n//2)

    total_white = w1 + w2 + w3 + w4
    total_blue = b1 + b2 + b3 + b4

    return (total_white, total_blue)
    
    
def answer():
    n = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    white, blue = recur(arr, 0, 0, n)
    print(white)
    print(blue)

answer()