import sys

sys.stdin = open('input.txt', "r")

def recur(sum_count, depth): # 4
    if sum_count == depth:
        return 1
    if sum_count > depth:
        return 0
    # print(f'sum_count : {sum_count}, depth : {depth}')
    return recur(sum_count+1, depth) + recur(sum_count+2, depth) + recur(sum_count+3, depth)

n = int(sys.stdin.readline())

for i in range(n):
    input_number = int(sys.stdin.readline())
    print(recur(0, input_number))


