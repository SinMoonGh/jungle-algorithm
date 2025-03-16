import sys

sys.stdin = open('input.txt', "r")

a = int(input())
b = int(input())
c = int(input())

mul = a * b * c
str_mul = str(mul)

sum0 = 0
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0
sum7 = 0
sum8 = 0
sum9 = 0


for i in str_mul:    
    if i == '0':
        sum0+=1
    if i == '1':
        sum1+=1
    if i == '2':
        sum2+=1
    if i == '3':
        sum3+=1
    if i == '4':
        sum4+=1
    if i == '5':
        sum5+=1
    if i == '6':
        sum6+=1
    if i == '7':
        sum7+=1
    if i == '8':
        sum8+=1
    if i == '9':
        sum9+=1

for answer in sum0, sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8, sum9:
    print(answer)