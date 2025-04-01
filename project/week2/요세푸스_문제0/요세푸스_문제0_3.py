import sys
from collections import deque

sys.stdin = open('input.txt', "r")

dq = deque()
answer = []

def kill(y):
    for _ in range(0, y-1):
        dq.append(dq.popleft())
    answer.append(dq.popleft())

def input_data(x):
    for i in range(1, x+1):
        dq.append(i)

x, y = map(int, sys.stdin.readline().split())

input_data(x)

while True:
    if len(dq) == 0:
        break

    kill(y)

print("<" + ", ".join(map(str, answer)) + ">")