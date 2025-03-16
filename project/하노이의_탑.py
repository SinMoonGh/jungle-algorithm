import sys

sys.stdin = open('input.txt', "r")

n = int(input())

def hanoi(n, start, end, mid):    
    if n == 0:
        # print(start, end)
        return
    
    hanoi(n-1, start, mid, end)
    print(start, end)
    hanoi(n-1, mid, end, start)

print(2**n-1)
if n <= 20:
    hanoi(n, 1, 3, 2)
