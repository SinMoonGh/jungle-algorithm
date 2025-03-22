import sys

sys.stdin = open('input.txt', "r")

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

# -------------------------------------
# print(arr)

# sort 정렬 메서드 사용하기

# for i in sorted(arr):
#     print(i)

# 버블 sort
def bubble_sort(arr):
    for i in range(len(arr)):
        left = 0
        right = 1
        swiching(arr, left, right, len(arr) - 1 - i)

    for i in arr:
        print(i)
         
    
def swiching(arr, left, right, end):
    for _ in range(end):
        if arr[left] > arr[right]:  # 큰 값을 오른쪽으로 이동
                arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right += 1
    

    
# arr = [9, 1, 5, 7, 8, 3, 2, 6, 4]
bubble_sort(arr)


