class Stack:
    def __init__(self):
        self.stack = []  # 스택을 리스트로 구현

    def push(self, item):
        """스택에 요소 추가 (삽입)"""
        self.stack.append(item)

    def pop(self):
        """스택에서 요소 제거 (삭제)"""
        if not self.is_empty():
            return self.stack.pop()
        return None  # 스택이 비었을 때 예외 처리

    def peek(self):
        """스택의 최상단 요소 확인 (삭제하지 않음)"""
        if not self.is_empty():
            return self.stack[-1]
        return None  # 스택이 비었을 때 예외 처리

    def is_empty(self):
        """스택이 비어있는지 확인"""
        return len(self.stack) == 0

    def size(self):
        """스택의 크기 반환"""
        return len(self.stack)

    def print_stack(self):
        """스택 요소 출력 (디버깅용)"""
        print("Stack:", self.stack)

# # 스택 사용 예제
# stack = Stack()
# stack.pop
# stack.push(20)
# stack.push(30)

# stack.print_stack()  # Stack: [10, 20, 30]

# print("Pop:", stack.pop())  # Pop: 30
# print("Peek:", stack.peek())  # Peek: 20
# print("Is Empty:", stack.is_empty())  # False
# stack.print_stack()  # Stack: [10, 20]
