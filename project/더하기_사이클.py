import sys

sys.stdin = open('input.txt', "r")

n = int(sys.stdin.readline())
nx_ = n // 10 # 2
ny_ = n % 10 # 6

count = 0

def recur(int_sum, nx, ny, count):# 26 2
    # if count == 4:
    #     return 0

    if n == int_sum and count != 0:
        print(count)
        return 0
    
    int_sum = str(ny)[-1]+str(nx + ny)[-1] #68
    int_sum = int(int_sum)# 정수로 변환
    nx = int_sum // 10 # 6
    ny = int_sum % 10 # 8

    # print(nx, ny)
    # print(int_sum)

    count += 1

    recur(int_sum, nx, ny, count)

# ## 사이클
# nx = ny
# ny = int_sum
recur(n, nx_, ny_, count)