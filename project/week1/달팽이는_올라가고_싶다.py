import sys

sys.stdin = open('input.txt', "r")

# a,b,v = map(int, input().split())
import math
a,b,v = map(int, sys.stdin.read().split())

# try 1-------------------------------------

# race = 0
# day = 0

# while(True):
#     day += 1
#     race += a

#     if race > v:
#         print(day)
#         break

#     race -= b

# try 2------------------------------------------

# stack_count = int((v/a)+1)
# stack = a * stack_count
# pop = b*stack_count

# if (v-(stack-pop)) > v:
#     print("이대로 승리")
# else:
#     ((v-(stack-pop))/a)+1
#     print(((v-(stack-pop))/a)+1)

# try3----------------------------------

day = math.ceil((v-a)/(a-b)) + 1
print(day)