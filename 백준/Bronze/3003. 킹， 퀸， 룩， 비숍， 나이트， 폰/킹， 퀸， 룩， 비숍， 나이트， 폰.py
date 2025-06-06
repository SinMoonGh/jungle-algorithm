arr = [1,1,2,2,2,8]
input_pice = list(map(int, input().split()))
anser = 0

for i in range(len(input_pice)):
    anser = arr[i] - input_pice[i]
    print(anser, end=' ')