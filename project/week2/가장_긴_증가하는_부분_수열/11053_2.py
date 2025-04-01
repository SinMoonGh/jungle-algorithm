import sys

sys.stdin = open('project/week2/input.txt', "r")

def find(arr, num):
    """이분 탐색"""
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start+end)//2

        if arr[mid] >= num:
            end = mid - 1
        elif arr[mid] < num:
            start = mid + 1

    return start

def answer():
    # arr = [4,5,36,13,7,2]
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    result = []

    for num in arr:
        if len(result) == 0:
            result.append(num)
        elif result.count(num) == 0:
            result[find(result, num)] = num
        elif result[len(result)-1] < num:
            result.append(num)

answer()