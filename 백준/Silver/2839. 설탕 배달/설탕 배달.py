

import sys

input_S = sys.stdin.readline

def answer(n):
    five = n // 5

    while five >= 0:
        remain = n - (five * 5)

        if remain % 3 == 0:
            three = remain // 3
            answer = five + three
            return answer
        else:
            five -= 1
    
    return -1

n = int(input_S())

print(answer(n))