# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

import sys

sys.stdin = open('input.txt', "r")

n = int(input())

for i in range(n): # 1
    for j in range(i): # 
        print("*", end='')
    print("*")

# for i in range(n):
#     print("*")qu