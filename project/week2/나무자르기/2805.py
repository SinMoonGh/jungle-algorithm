import sys

sys.stdin = open('input.txt', "r")

def tree(trees, need_h):
    start = 0
    end = max(trees)
    answer = 0

    while start <= end:
        mid = (start+end)//2
        tree_h = cut_tree(trees, mid)

        if tree_h >= need_h:
            answer = mid
            start = mid + 1
        elif tree_h < need_h:
            end = mid - 1
    return answer


def cut_tree(trees, mid):
    sum = 0
    for i in trees:
        if i - mid > 0:
            sum += (i - mid)
    return sum 

tree_count, tree_h = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

print(tree(arr, tree_h))