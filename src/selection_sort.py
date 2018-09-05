def find_smallest(arr, start=0):
    smallest = arr[start]
    smallest_index = start
    for i in range(start, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort(list_to_sort, in_place=False):
    if in_place:
        return selection_sort_in_place(list_to_sort)
    else:
        return selection_sort_new(list_to_sort)


# sorting in place
def selection_sort_in_place(list_to_sort):
    for i in range(len(list_to_sort)):
        smallest_index = find_smallest(list_to_sort, i)
        current_element = list_to_sort[i]
        list_to_sort[i] = list_to_sort[smallest_index]
        list_to_sort[smallest_index] = current_element
    return list_to_sort


# sorting and returning new array
def selection_sort_new(list_to_sort):
    result = []
    for i in range(len(list_to_sort)):
        smallest = find_smallest(list_to_sort)
        result.append(list_to_sort.pop(smallest))
    return result


print(selection_sort([6, 1, 5, 4, 3, 2, 7], True))
