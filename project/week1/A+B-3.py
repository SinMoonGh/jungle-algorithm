# https://itcrowd2016.tistory.com/81

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

import sys

sys.stdin = open('input.txt', "r")

n = int(input())

for i in range(n):
    a, b = map(int,input().split())
    print(a+b)
