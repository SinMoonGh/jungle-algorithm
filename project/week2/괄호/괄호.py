import sys

sys.stdin = open('input.txt', "r")

class Stack:
    def __init__(self):
        self.arr = []

    def push(self, num):
        self.arr.append(num)

    def pop(self):
        if self.empty() == True:
            print('NO')
            return False
        else:
            return self.arr.pop()

    def empty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False 


# def answer(test_case):
#     for i in test_case:
#         if i == '(':
#             stack.push('(')
#         if i == ')':
#             if stack.pop() == False:
#                 return 0
    
#     if len(stack.arr) == 0:
#         print('YES')
#     else:
#         print('NO')

def answer(test_case):
    if test_case == '(':
        stack.push('(')
    if test_case == ')':
        if stack.pop() == False:
            return 0
    if len(stack.arr) != 0:
        print("NO")          

test1 = '('
test2 = ')'
test3 = '()'
test4 = '())'

stack = Stack()

# n = int(sys.stdin.readline())
# input_list = [sys.stdin.readline() for _ in range(n)]

# for i in test4:
#     for j in i[:-1]:
#         answer(j)

for i in test4:
    answer(i)
