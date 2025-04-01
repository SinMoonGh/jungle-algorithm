class MaxHeap:
    def __init__(self):
        self.heap = []  # 인덱스 1부터 시작

    def insert(self, value):
        self.heap.append(value)
        idx = len(self.heap) - 1

        # 부모보다 크면 swap
        while idx > 1:
            parent = idx // 2
            if self.heap[idx] > self.heap[parent]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def pop(self):
        if len(self.heap) == 1:
            return None  # empty

        max_value = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()

        idx = 1
        while True:
            left = 2 * idx
            right = 2 * idx + 1
            largest = idx

            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == idx:
                break
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            idx = largest

        return max_value

    def peek(self):
        return self.heap[1] if len(self.heap) > 1 else None

h = MaxHeap()
h.insert(10)
h.insert(100)

h.insert(5)
h.insert(30)
h.insert(20)
print(h.heap)
