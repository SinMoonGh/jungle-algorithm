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

def koi_telecommunications(test_case):
    pass