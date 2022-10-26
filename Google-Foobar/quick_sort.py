["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]

sequence = [int]
def quick_sort(sequence):
    length = len(sequence)
    if length >= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []
    item_equal = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        elif item == pivot:
            item_equal.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] +item_equal+ quick_sort(items_greater)


print(quick_sort([1,1,1,1,1]))