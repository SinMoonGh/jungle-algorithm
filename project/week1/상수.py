import sys

sys.stdin = open('input.txt', "r")

a, b = map(str, input().split())
sum1 =0
sum2 = 0
count =0

g=0
p=0
t=0

arr = [0]*2

for i in a, b:
    count+=1

    g = i[2]
    p = i[1]
    t = i[0]
    
    if count == 1:
        sum1=g+p+t
    if count == 2:
        sum2 = g+p+t

if sum1 > sum2:
    print(sum1)
if sum2 > sum1:
    print(sum2)
    