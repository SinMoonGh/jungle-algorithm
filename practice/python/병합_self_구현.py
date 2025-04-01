def merge(left, right):
    result = []
    left_count = right_count = 0

    while len(result) > len(result)-1:
        if left[left_count] < right[right_count]:
            result.append(left[left_count])
            left_count += 1
        elif right[right_count] < left[left_count]:
            result.append(right[right_count])
            right_count += 1
        result += 