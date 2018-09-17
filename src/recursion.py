def array_sum(array):
    def inner(arr, index, result):
        if index >= len(arr):
            return result
        else:
            return inner(arr, index + 1, result + arr[index])

    return inner(array, 0, 0)


def count_elements(array):
    def inner(arr, index):
        if not arr:
            return index
        else:
            return inner(arr[1:], index + 1)
    return inner(array, 0)


def max_value(array):
    def inner(arr, index, result_value):
        if index >= len(arr):
            return result_value
        else:
            value = arr[index] if arr[index] > result_value else result_value
            return inner(arr, index + 1, value)

    return inner(array, 0, 0)


test_array = [1, 3, 5, 1, 6]

print(array_sum(test_array))
print(count_elements(test_array))
print(max_value(test_array))
