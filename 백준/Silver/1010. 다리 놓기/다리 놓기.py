import sys

input_s = sys.stdin.readline

def factorial(n):
    result = 1

    for i in range(2, n+1):
        result = result * i
        
    return result


def combination(m, n):
    numerator = factorial(m)
    denominator = factorial(n) * factorial(m - n)

    return numerator // denominator

num = int(input_s())

for _ in range(num):
    n, m = map(int, input_s().split())

    print(combination(m, n))