def quick_sort(array):
    if len(array) < 2:
        return array
    elif len(array) == 2:
        return array if array[0] < array[1] else [array[1], array[0]]

    pivot = array[0]
    less_then = []
    greater_than = []
    for element in array[1:]:
        if element <= pivot:
            less_then.append(element)
        else:
            greater_than.append(element)
    return quick_sort(less_then) + [pivot] + quick_sort(greater_than)


print(quick_sort([6, 6, 1, 5, 2, 7, 3, 9, 4]))
