import sys

sys.stdin = open('input.txt', "r")

# n = int(sys.stdin.readline())
# arr = [] # arr 스택이 1000만
# for i in range(n):
#     arr.append(int(sys.stdin.readline()))

# a = [0]*(max(arr)+1) #1001만

# for i in arr:
#     a[i] += 1

# # sorted_arr = [] # 1000만
# for i in range(len(a)):
#     for j in range(a[i]):
#         # sorted_arr.append(i)
#         print(i)

# # for i in sorted_arr:
# #     print(i)
# print(a)


#---------------재도전

n = int(sys.stdin.readline())
a = [0]*10001

for _ in range(n):
    num = int(sys.stdin.readline())
    a[num]+=1

for i in range(len(a)):
    if a[i] != 0:
        for j in range(a[i]):
            print(i)
