import sys

sys.stdin = open('input.txt', "r")

def search(arr, start, end, target):
    mid = (start+end)//2

    if arr[mid] == target:
        return 1
    if start >= end:
        return 0
    if target < arr[mid]:
        end = mid-1
    if target > arr[mid]:
        start = mid+1    
    
    return search(arr, start, end, target)

# 입력
n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))

n_arr = sorted(n_arr)

for i in m_arr:
    print(search(n_arr, 0, len(n_arr)-1, i))
    