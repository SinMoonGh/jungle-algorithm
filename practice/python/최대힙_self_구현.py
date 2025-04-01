def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # 최댓값을 맨 뒤로
        heapify(arr, i, 0)    


def heapify(arr, heap_size, parent):
    # 내가 생각한 부분은 'heap_sort의 동작까지 알 필요 없다. 그래서 down_heap을 감춘거다' 라고 생각함.
    largest = parent
    cl = parent * 2 +1
    cr = parent * 2 +2

    if cl < heap_size and arr[cl] > arr[largest]:
        largest = cl
    
    if cr < heap_size and arr[cr] > arr[largest]:
        largest = cr

    if largest != parent:
        arr[parent], arr[largest] = arr[largest], arr[parent]
        heapify(arr, heap_size, largest)


arr = [10, 9, 5, 8, 3, 2, 4, 6, 7, 1]
# arr = [10,20,30,12]

heap_sort(arr)

print(arr)
