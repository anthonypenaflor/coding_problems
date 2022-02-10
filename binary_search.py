def binary_search(array, target):
    # Write your code here.
    return binary_search_helper(array, target, 0, len(array) - 1)


def binary_search_helper(array, target, left, right):
    if left > right:
        return -1

    middle_val = (left + right) // 2
    potential_match = array[middle_val]

    if target == potential_match:
        return middle_val
    elif target < potential_match:
        return binary_search_helper(array, target, left, middle_val - 1)
    else:
        return binary_search_helper(array, target, middle_val + 1, right)


if __name__ == '__main__':
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 33
    binary_search(array, target)
