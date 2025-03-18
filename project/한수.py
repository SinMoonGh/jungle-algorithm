import sys

sys.stdin = open('input.txt', "r")

n = input()
sum_n = 0

if len(n) == 1:
    # print("일의 자리")
    sum_n = int(n)
if len(n) == 2:
    # print("십의 자리")
    sum_n = int(n)
if len(n) == 3:
    # print("백의자리")
    sum_n = 99
    for i in range(100, int(n)+1):
        str_i = str(i)
        for a, b, c in zip(str_i[0], str_i[1], str_i[2]):
            a = int(a)
            b = int(b)
            c = int(c)
            if c-b == b - a:
                # print(i)
                sum_n += 1
if len(n) == 4:
    sum_n = 144

print(sum_n)