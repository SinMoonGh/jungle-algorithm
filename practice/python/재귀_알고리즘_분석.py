from Stack import Stack

## case 1
def recur(n: int):
    if n > 0:
        recur(n-1)
        print(n)
        recur(n-2)

## case 2
def recur(n: int):
    if n > 0:
        recur(n-2)
        print(n)
        recur(n-1)

## case 3
def recur(n: int):
    while n > 0:
        recur(n-1)
        print(n)
        n = n-2

## case 4
def recur(n: int):
    s = Stack()

    while(True):
        if n > 0:
            s.push(n)
            n = n - 1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n = n-2
            continue
        break

recur(4)