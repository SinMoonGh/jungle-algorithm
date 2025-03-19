import sys
import random

sys.stdin = open('input.txt', "r")

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

left = 0
right = len(arr)-1

def median_of_three(arr, left, right):
    mid = (left + right) // 2
    candidates = [arr[left], arr[mid], arr[right]]
    candidates.sort()
    return candidates[1]  # 중앙값 반환

# quick sort - recur

def quick_sort_recur(left, right):
    pl = left
    pr = right
    pivot_idx = random.randint(0, 4)
    # pivot = int((left+right)/2)
    pivot_value = arr[pivot_idx]

    while(True):
        if pl >= pr:
            break

        while(pl <= right and pr >= left):
            if arr[pl] < pivot_value:
                pl += 1
            else:
                break

        while(pl <= right and pr >= left):
            if arr[pr] > pivot_value:
                pr -= 1
            else:
                break

        if pl <= pr:  # 교환 후, 인덱스 이동
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1

    if left < pr:
        quick_sort_recur(left, pr)
    if right > pl:
        quick_sort_recur(pl, right)

    # print(f'pl : {pl}, pr : {pr}, pivot : {pivot}')


# quick_sort_stack

def quick_sork_stack(left, right):
    stack = [(0, len(arr)-1)]
    
    while stack:
        left, right = stack.pop()
        pl = left
        pr = right
        pivot_value = median_of_three(arr, left, right)

        while(True):
            # print(f'left : {left}, right : {right}, stack : {stack}')

            if pl >= pr:
                break

            while arr[pl] < pivot_value:
                pl += 1

            while arr[pr] > pivot_value:
                pr -= 1

            if pl <= pr:  # 교환 후, 인덱스 이동
                arr[pl], arr[pr] = arr[pr], arr[pl]
                pl += 1
                pr -= 1

            if (pr-left) > (right-pl):
                print("왼쪽 먼저")
                if left < pr:
                    stack.append((left, pr))
                if pl < right:
                    stack.append((pl, right))
            else:
                print("오른쪽 먼저")
                if pl < right:
                    stack.append((pl, right))
                if left < pr:
                    stack.append((left, pr))
            # print(arr)


# 병합 정렬로 도전

arr = sorted(arr)
for i in arr:
    print(i)