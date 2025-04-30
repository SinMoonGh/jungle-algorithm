m = int(input())
numbers = list(map(int, input().split()))

max_number = max(numbers)
sum = 0
for i in range(m):
    sum += ((numbers[i] / max_number) * 100)

avg = sum / m
print(avg)