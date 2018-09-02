def binary_search(list, item):
    length = len(list)
    if length == 0:
        return None

    middleIndex = (length - 1) // 2
    if list[middleIndex] == item:
        return middleIndex
    elif list[middleIndex] < item:
        return binary_search(list[:middleIndex], item)
    elif list[middleIndex] > item:
        return binary_search(list[middleIndex:], item)


print(binary_search([2, 4, 1, 5, 6, 8], 8))
