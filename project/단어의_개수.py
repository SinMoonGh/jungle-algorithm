import sys

sys.stdin = open('input.txt', "r")

n = list(map(str, input().split()))

print(len(n))