import sys

sys.stdin = open('input.txt', "r")

n = int(input())
arr = list(map(int, input().split()))
sum = 0

# try -------------------------
# for i in arr:
#     if i == 1:
#         continue
#     if i == 2 or i == 3 or i == 5 or i == 7:
#         sum+=1
#     if i % 2 == 0:
#         continue
#     if i % 3 == 0:
#         continue
#     if i % 5 == 0:
#         continue
#     if i % 7 == 0:
#         continue 
#     if i % int(i**0.5) == 0:
#         print(i)   
#     sum += 1
#     # print(i)

# print(sum)

# try2------------------------------

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
#     if int(i % i**0.5) == 0:
#         continue 
      
#     # print(i)
# print(int(169**0.5))
# if int(169 % int(169**0.5)) == 0:
#     print('dd') 

# try 3--------------------

for i in arr:
    if i < 2:
        continue
    
    is_true = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            is_true = False
            break

    if is_true:
        sum+=1
print(sum)
    