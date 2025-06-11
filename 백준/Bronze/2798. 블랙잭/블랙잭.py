Max = 0
Sum = 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            Sum = arr[i] + arr[j] + arr[k]
            # print("arr[i] : ", arr[i])
            # print("arr[j] : ", arr[j])            
            # print("arr[k] : ", arr[k])
            
            # print("Sum : ", Sum)
            
            if m >= Sum and Sum > Max:
                Max = Sum          
                # print("Max : ", Max)
                
            
print(Max)