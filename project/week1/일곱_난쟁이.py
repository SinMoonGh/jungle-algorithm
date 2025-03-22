import sys

sys.stdin = open('input.txt', "r")

arr = []
answer = []
key = 100
arr_1 = 0
arr_2 = 0

for _ in range(9):
    arr.append(int(sys.stdin.readline()))

# arr = sorted(arr, reverse=True)
# for i in arr:
#     if (key - i) >= 0:        
#         key = key - i
#         answer.append(i)
# print(sorted(answer))


# 재 도전
key_sum = sum(arr)

for i in range(len(arr)):
    for j in range(len(arr)):        
        if key_sum - (arr[i]+arr[j]) == 100 and arr[i]!=arr[j]:
            arr_1 = i
            arr_2 = j


for i in range(len(arr)):
    if i != arr_2 and i != arr_1:
        answer.append(arr[i])

for i in sorted(answer):
    print(i)