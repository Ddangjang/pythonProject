array = [5, 3, 2, 1, 6, 8, 7, 4]


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]
    print(array)
    print('left_arary', left_array)
    print('right_arary', right_array)
    return merge(merge_sort(left_array), merge_sort(right_array))