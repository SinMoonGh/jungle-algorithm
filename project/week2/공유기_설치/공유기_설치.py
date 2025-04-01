import sys

sys.stdin = open('project/week2/input.txt', "r")

def route_count(arr, mid):
    before_r = arr[0]
    r_count = 1

    for i in range(1, len(arr)):
        cur_r = arr[i]
        
        if cur_r - before_r >= mid:
            r_count += 1
            before_r = arr[i]

    return r_count            


def search(arr, input_counting_r):
    first_h = 1
    last_h = arr[-1] - arr[0]
    result = 0

    while first_h <= last_h:
        mid = (last_h + first_h)//2
        r_count = route_count(arr, mid)
        
        if r_count < input_counting_r:
            last_h = mid - 1
        elif r_count >= input_counting_r:
            result = mid
            first_h = mid+1       

    return result


n, count = list(map(int, sys.stdin.readline().split()))
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr = sorted(arr)

print(search(arr, count))
