def heap_sort(arr):
    n = len(arr)

    # 1단계: 최대 힙 만들기 (Bottom-up 방식)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 2단계: 하나씩 루트(최댓값)를 뒤로 보내고, 다시 힙 정렬
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # 최댓값을 맨 뒤로
        heapify(arr, i, 0)               # 크기를 줄이고 힙 재정렬

    return arr

# 힙 정렬의 핵심: heapify
def heapify(arr, heap_size, parent):
    largest = parent
    left = 2 * parent + 1
    right = 2 * parent + 2

    # 왼쪽 자식이 더 크면 largest 갱신
    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 더 크면 largest 갱신
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    # 부모보다 큰 자식이 있으면 교환 + 재귀 호출
    if largest != parent:
        arr[parent], arr[largest] = arr[largest], arr[parent]
        heapify(arr, heap_size, largest)


nums = [10, 9, 5, 8, 3, 2, 4, 6, 7, 1]
sorted_nums = heap_sort(nums[:])  # 원본 보존
print(sorted_nums)  # [1, 2, 3, 4, 5, 7, 8]