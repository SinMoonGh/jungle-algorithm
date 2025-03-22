# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
a = int(input())

if a>89 and a <=100: #90, 100
    print("A")
if a>79 and a <=89: #80, 89
    print("B")
if a>69 and a <=79: #70, 79
    print("C")
if a>59 and a <=69: #60, 69
    print("D")
if a<=59: #59이하
    print("F")
