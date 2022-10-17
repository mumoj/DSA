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

    for item in sequence:
        if item #greater than pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)