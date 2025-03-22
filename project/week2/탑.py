import sys

sys.stdin = open('input.txt', "r")

# test1 = [1,2,3]
# test2 = [2,1,3]
# test3 = [3,2,1]
# test4 = [6, 9, 5, 7, 4]

def koi_telecommunications(test_case):
    signal = []
    pivot = 0
    test_case = list(reversed(test_case))

    for index in range(1, len(test_case)+1):
        pop_data = test_case.pop()
        print(index, pop_data)

        if pop_data > pivot:
            signal.append(0)
            pivot = pop_data

            pivot_index = index
        else:
            signal.append(pivot_index)

    # print(pivot, pop_data)
    print(signal)  

def koi_telecommunications_ver2(test_case):
    left = 0
    signal = []
    answer = []

    for i in enumerate(test_case, start=1):
        if left == 0:
            signal.append(i)
            answer.append(0)
            left = i[1]
        else:
            while signal and signal[-1][1] < i[1]:
                print(signal[-1][1], i[1])
                signal.pop()
                signal.append(i)
                answer.append(0)
            if signal[-1][1] > i[1]:
                signal.append(i)
                answer.append(i[0]-1) 
        # print(signal)
    return answer

n = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))

for i in koi_telecommunications_ver2(input_list):
    print(i, end=' ')