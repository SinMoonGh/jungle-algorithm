import sys

sys.stdin = open('input.txt', "r")

n = int(input())
stu_list = [list(map(int,input().split())) for _ in range(n)]

for stu_class in stu_list:
    stu_sum = 0
    class_avg = 0
    luckey = 0
    for stu_score in stu_class:
        stu_sum += stu_score
    class_avg = (stu_sum-stu_class[0]) / (stu_class[0])

    for stu_score in stu_class[1:]:
        # print(stu_score)
        if class_avg < stu_score:
            luckey += 1
            # print(class_avg, stu_score)
            # print(stu_class)
            # print(stu_class, luckey)

    print(f'{round(luckey/stu_class[0]*100, 3):.3f}%')