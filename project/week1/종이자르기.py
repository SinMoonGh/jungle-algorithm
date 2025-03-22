import sys

sys.stdin = open('input.txt', "r")

x, y = map(int,input().split())
n = int(input())

arr_l = []
arr_m = []
widths = []
heigh = []

for _ in range(n):
    l, m = map(int,input().split())
    if l == 1:
        arr_l.append(m)
    if l == 0:
        arr_m.append(m)

arr_l = [0] + sorted(arr_l) + [x]
arr_m = [0] + sorted(arr_m) + [y]

for i in range(len(arr_l)-1, 0, -1):
    widths.append(arr_l[i] - arr_l[i-1])

for i in range(len(arr_m)-1, 0, -1):
    heigh.append(arr_m[i] - arr_m[i-1])

# print(x, y, n)
# print(f'세로 : {arr_l}, 가로 : {arr_m}')
# print(f'너비 : {widths}, 높이 : {heigh}')
print(max(widths)* max(heigh))