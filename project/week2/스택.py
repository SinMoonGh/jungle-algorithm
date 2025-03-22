import sys

sys.stdin = open('input.txt', "r")

class Stack:
    def __init__(self):
        self.arr = []  

    def push(self, num):
        self.arr.append(num)

    def pop(self):
        if self.empty() == 1:
            return -1
        else:
            return self.arr.pop()

    def size(self):
        return len(self.arr)

    def empty(self):
        if len(self.arr) == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.empty() == 1:
            return -1
        else:
            return self.arr[-1]

n = int(sys.stdin.readline())
command = [list(map(str,input().split())) for _ in range(n)]

stack = Stack()

for i in command:
    if i[0] == 'push':
        stack.push(i[1])
    if i[0] == 'pop':
        print(stack.pop())
    if i[0] == 'size':
        print(stack.size())
    if i[0] == 'empty':
        print(stack.empty())
    if i[0] == 'top':
        print(stack.top())
    