def array_sum(array):
    def inner(arr, index, result):
        if index >= len(arr):
            return result
        else:
            return inner(arr, index + 1, result + arr[index])

    return inner(array, 0, 0)


print(array_sum([1, 3, 5, 1, 6]))


# def count_elements(array):
#    def inner(arr, index):
#        if len(arr) >= index

def max_value(array):
    def inner(array, index, result_value):
        if index >= len(array):
            return result_value
        else:
            value = array[index] if array[index] > result_value else result_value
            return inner(array, index + 1, value)

    return inner(array, 0, 0)


print(max_value([1, 3, 5, 8, 6]))
