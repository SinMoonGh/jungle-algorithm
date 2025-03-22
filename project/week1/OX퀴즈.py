import sys

sys.stdin = open('input.txt', "r")

n = int(input())
data = sys.stdin.read().splitlines()
data_count = 0
score_list = [0]*(n+1)

for i in data:
    score = 0
    data_count += 1
    for ox, OX_count in zip(i, range(len(i))):
        if ox == 'O':
            score += 1
            score_list[data_count] += score            
        if ox == 'X':            
            score = 0

for i in range(1,len(score_list)):
    print(score_list[i])
            