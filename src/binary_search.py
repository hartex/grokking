def binary_search(list_to_search, item):
    def inner(list_to_search, item, start, end):
        if start > end:
            return None

        middle_index = (end + start) // 2
        middle_item = list_to_search[middle_index]
        if middle_item == item:
            return middle_index
        elif item < middle_item:
            return inner(list_to_search, item, start, middle_index - 1)
        else:
            return inner(list_to_search, item, middle_index + 1, end)

    return inner(list_to_search, item, 0, len(list_to_search))


print(binary_search([1, 2, 4, 5, 6, 8, 10], 10))
