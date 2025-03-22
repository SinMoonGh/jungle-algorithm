# 한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.


# x는 0으로 가든지 w로 가든지
# y는 0으로 가든지 h로 가든지
# 절댓값이 나와야 함으로 음수는 -곱해주고, 양수는 그대로

# x,y,w,h=map(int,input().split())
# print(min(x,y,w-x,h-y))

# array = [0] * 4
# min = 2000

# array[0] = abs(x-0)
# array[1] = abs(w - x)
# array[2] = abs(y - 0)
# array[3] = abs(h - y)

# for i in range(0,4):
#     if min > array[i]:
#         min = array[i]

# print(min)
