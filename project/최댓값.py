import sys

sys.stdin = open('input.txt', "r")

a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())
a6 = int(input())
a7 = int(input())
a8 = int(input())
a9 = int(input())

max = 0
count = 0

for i in a1, a2, a3, a4, a5, a6, a7, a8, a9:
    count += 1
    if max < i:
        max = i
        max_count = count

print(max)
print(max_count)
