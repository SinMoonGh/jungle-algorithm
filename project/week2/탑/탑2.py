import sys

sys.stdin = open('input.txt', "r")

stack = []
answer = []

top_stack_index= -1
stack_num_index = 0
stack_hei_index = 1

def top_list(top_num, top_hei):
    t_f = True
    while True:
        if len(stack) == 0:
            stack.append([top_num, top_hei])
            answer.append(0)
            break
        elif stack[top_stack_index][stack_hei_index] > top_hei:
            answer.append(stack[top_stack_index][stack_num_index])
            stack.append([top_num, top_hei])
            break
        elif stack[top_stack_index][stack_hei_index] <= top_hei:
            stack.pop()

n = int(sys.stdin.readline())
top_data = list(map(int, sys.stdin.readline().split()))

for i in range(1, n+1):
    top_list(i, top_data[i-1])
    # print(i)

for i in answer:
    print(i, end=' ')



# top_list(1, 6)
# print(f'stack: {stack}')

# top_list(2, 9)
# print(f'stack: {stack}')

# top_list(3, 5)
# print(f'stack: {stack}')

# top_list(4, 7)
# print(f'stack: {stack}')

# top_list(5, 4)
# print(f'stack: {stack}')

# print(answer)