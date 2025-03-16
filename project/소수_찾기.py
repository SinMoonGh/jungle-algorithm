import sys

sys.stdin = open('input.txt', "r")

n = int(input())
arr = list(map(int, input().split()))
sum = 0

for i in arr:
    if i == 1:
        continue
    if i == 2 or i == 3 or i == 5 or i == 7:
        sum+=1
    if i % 2 == 0:
        continue
    if i % 3 == 0:
        continue
    if i % 5 == 0:
        continue
    if i % 7 == 0:
        continue    
    sum += 1
    # print(i, sum)

print(sum)

# for i in range(1,1000):
#     if i == 1:
#         continue
#     if i % 2 == 0:
#         continue
#     if i % 3 == 0:
#         continue
#     if i % 5 == 0:
#         continue
#     if i % 7 == 0:
#         continue    
#     print(i)