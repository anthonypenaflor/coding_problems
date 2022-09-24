# O(n*n^2) time | O(n*n^2) space
def powerset(array):
    subsets = [[]]
    for num in array:
        for i in range(len(subsets)):
            current_subset = subsets[i]
            subsets.append(current_subset + [num])
    return subsets


if __name__ == '__main__':
    sample = [1, 2, 3]
    powerset(sample)
