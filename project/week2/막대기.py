import sys

sys.stdin = open('input.txt', "r")

arr1 = [6,9,7,6,4,6]
arr2 = [5,4,3,2,1]
arr3 = [0]
arr4 = [5, 3, 1, 100, 33, 77]
arr5 = [7,7,7,8,7,7,7,6]
arr6 = [7, 8, 6]

def push_bar(push_list):
    count = 0
    pivot = push_list.pop()

    if pivot > 0:
        count += 1

    for _ in range(len(push_list)):
        pop_data = push_list.pop()
        if pivot >= pop_data:
            continue
        else:
            pivot = pop_data
            count += 1

    print(count)

# arr3 = []
# n = int(sys.stdin.readline())

# for i in range(n):
#     input_num = int(sys.stdin.readline())
#     arr3.append(input_num)

push_bar(arr2)