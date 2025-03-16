import sys

sys.stdin = open('input.txt', "r")

arr = list(range(1, 10000001))

def solve(a: list):
    answer = 0

    # sum_a = [i for i in a]
    answer = sum(a)

    return answer

print(solve(arr))
