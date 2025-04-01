import sys
from collections import deque

sys.stdin = open('input.txt', "r")

dq = deque()

def answer():
    if len(dq) >= 2:
        # 앞에껄 뺀다.
        dq.popleft()

        # 앞에껄 뺐다가 left에 저장한다.
        left = dq.popleft()

        # 큐 끝에 추가한다.
        dq.append(left)

# arr = [1,2,3,4]
n = int(sys.stdin.readline())

# dq = [1,2,3,4]
for i in range(1, n+1):
    dq.append(i)

queue_start = True
while queue_start:
    answer()

    if len(dq) == 1:
        print(dq[0])
        queue_start = False
    
# print(dq)