# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
import sys

sys.stdin = open('input.txt', "r")

n = int(sys.stdin.readline())

# for i in range(2, n+1):
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i*j}')

for j in range(1, 10):
    print(f'{n} * {j} = {n*j}')