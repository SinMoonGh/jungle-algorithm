import sys

# sys.stdin = open('input.txt', "r")

class LingBuffer:
    def __init__(self, capacity, turn):
        self.queue = [None]*(capacity+1)
        self.front = 0
        self.rear = 0
        self.turn = turn
    
    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False
        
    def is_full(self):
        if (self.front == (self.rear + 1) % len(self.queue)):
            return True
        else:
            return False
        
    def enqueue(self, num):
        if self.is_full() == False:
            self.queue[self.rear] = num
            self.rear = (self.rear + 1) % len(self.queue)
        else:
            return False
        
    def dequeue(self):
        if self.is_empty() == False:
            self.front = (self.front + self.turn) % len(self.queue)

            # 값이 들어있는 index를 만날 때까지 순회
            while self.queue[self.front] is None:
                if self.is_empty() == True:
                    break
                self.front = (self.front + 1) % len(self.queue)

            value = self.queue[self.front]
            self.queue[self.front] = None
            return value
        else:
            return False

arr = [1,2,3,4]
ling_buffer = LingBuffer(len(arr), 3)

# 링버퍼에 데이터 할당
def input_data():
    for i in arr:
        ling_buffer.enqueue(i)

# 사람 제거하기
def kill():
    return ling_buffer.dequeue()

def answer():
    result = []
    input_data()

    while ling_buffer.is_empty() is False:
        result.append(kill())
    
    return result

print(answer())