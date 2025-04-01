import sys
from collections import deque

sys.stdin = open('input.txt', "r")

dq = deque()

def cammend_queue(cammend, input_data = 0):
    if cammend == "push":
        dq.append(input_data)
    if cammend == "pop":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    if cammend == "size":
        print(len(dq))
    if cammend == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    if cammend == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    if cammend == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])

n = int(sys.stdin.readline())
# arr = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]

for _ in range(n):
    input_data = list(map(str, sys.stdin.readline().split()))
    
    if len(input_data) == 1:
        cammend_queue(input_data[0])
    else:
        cammend_queue(input_data[0], input_data[1])



# cammend_queue('push', 3)
# cammend_queue('push', 4)
# cammend_queue('push', 5)
# cammend_queue('pop')
# cammend_queue('front')
# cammend_queue('back')
# cammend_queue('size')
# cammend_queue('empty')