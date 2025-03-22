import sys

sys.stdin = open('input.txt', "r")

class Stack:
    def __init__(self):
        self.arr = []

    def push(self, num):
        self.arr.append(num)

    def pop(self):
        if self.empty() == True:
            return False
        else:
            return self.arr.pop()

    def empty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False 


def answer(test_case):
    stack = Stack()

    for i in test_case:
        if i == '\n':
            continue
        if i == '(':
            stack.push('(')
        if i == ')':
            if stack.pop() == False:
                return False
            
    if len(stack.arr) != 0:
        return False
    
    return True

test1 = ['(']
test2 = [')']
test3 = ['(', ')']
test4 = ['(', ')', ')']
test5 = ['(', '(', ')', ')', '(', ')', ')']
test6 = ['(', '(', '(', '(', ')', '(', ')', ')', '(', ')']
test7 = ['(', '(', ')', '(', ')', ')', '(', '(', '(', ')', ')', ')']

# print(answer(test7))

n = int(sys.stdin.readline())
for i in range(n):
    input_data = list(map(str, sys.stdin.readline()))
    if answer(input_data) == True:
        print('YES')
    else:
        print('NO')