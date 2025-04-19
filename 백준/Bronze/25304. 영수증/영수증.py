total_mon = int(input())
n = int(input())
pri_sum = 0

for i in range(n):
    price, count = map(int, input().split())

    pri_sum += (price*count)

if pri_sum == total_mon:
    print("Yes")
else:
    print("No") 