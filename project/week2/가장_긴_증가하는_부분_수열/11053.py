import sys

sys.stdin = open('project/week2/input.txt', "r")

def bisect_left(temp, target):
    left = 0
    right = len(temp)-1

    while left <= right:
        mid = (left+right) // 2

        if temp[mid] > target:
            right = mid - 1
        elif temp[mid] <= target:
            left = mid + 1

    return left

def answer(arr):
    temp_list = []
    
    for i in arr:
        if len(temp_list) != 0 and temp_list.count(i) == 0:
            if temp_list[-1] < i:
                temp_list.append(i)
            else:
                left = bisect_left(temp_list, i)
                temp_list[left] = i
        elif len(temp_list) == 0:
            temp_list.append(i)

    print(temp_list)
    return len(temp_list)

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

print(answer(arr))