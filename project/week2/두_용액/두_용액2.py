import sys

sys.stdin = open('project/week2/input.txt', "r")

def two_point(arr):
    left =0
    right = len(arr)-1
    min_value = None
    pair = None    

    while left < right:
        sum_data = arr[left] + arr[right]

        if min_value == None:
            pair = [arr[left], arr[right]]
            min_value = abs(sum_data)
        else:
            if min_value > abs(sum_data):
                pair = [arr[left], arr[right]]
                min_value = abs(sum_data)

        if sum_data < 0:    
            left += 1            
        elif sum_data > 0:
            right -= 1
        else:
            break

    return pair

def answer():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr = sorted(arr)

    ans = two_point(arr)
    print(ans[0], ans[1])

answer()