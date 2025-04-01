import sys
from collections import deque

# sys.stdin = open('input.txt', "r")

dq = deque()
# 링버퍼에 데이터 할당
def input_data(arr):
    for i in arr:
        dq.append(i)

def kill(arr, turn):
    dq.remove(arr[turn-1])

def rearrange():
    data = dq.popleft()
    dq.append(data)

# 풀이 시작
arr = [1,2,3,4,5,6,7]
turn = 3

input_data(arr)
kill(arr, turn=turn)
rearrange()
print(dq)