import sys

input_s = sys.stdin.readline

def answer(n):
    count = n // 5

    while count >= 0:
        remain = n - (count * 5)

        if remain % 2 == 0:
            count += (remain // 2)
            return count
        else:
            count -= 1

    return -1

n = int(input_s())
print(answer(n))