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

n = int(sys.stdin.readline())
test_num = [int(sys.stdin.readline()) for _ in range(n)]  
 
# print(test_num)
    
stack = Stack()

for num in test_num:
    if num != 0:
        stack.push(num)
    if num == 0:
        stack.pop()

print(sum(stack.arr))