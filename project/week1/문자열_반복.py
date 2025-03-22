import sys

sys.stdin = open('input.txt', "r")

n = int(input())

for i in range(n):
    re, spa=map(str, input().split())
    for j in spa:
        for _ in range(int(re)):
            print(j, end='')
    print()