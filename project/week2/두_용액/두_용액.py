import sys

sys.stdin = open('project/week2/input.txt', "r")

def bi_search(arr, i, min_value):
    left = 0
    right = len(arr)-1
    target = -1 * i

    while left <= right:
        mid = (left+right)//2

        if i == arr[mid]:
            if mid < len(arr)-1:
                mid += 1
            else:
                break
        elif i > arr[mid]:
            left = mid + 1
        elif i <= arr[mid]:
            right = mid - 1

    return mid


def best_pair():
    if min_value > abs(i - arr[mid]):
            min_value = abs(i - arr[mid])


def answer():
    arr = [-2, 4, -99, -1, 98]
    arr = sorted(arr)
    min_value = 10000

    for i in arr:
        bi_search(arr, i, min_value)

