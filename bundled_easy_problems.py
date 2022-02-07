# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # array = [12, 3, 1, 2, -6, 5, -8, 6]
    sequence = [1, -6]
    # targetSum = 0

    """Sum of three numbers problem"""
    # for i in range(len(array) - 1):
    #     numOne = array[i]
    #     for j in range(i + 1, len(array)):
    #         numTwo = array[j]
    #         for k in range(j + 1, len(array)):
    #             numThree = array[k]
    #             if numOne + numTwo + numThree == targetSum:
    #                 print(numOne, numTwo, numThree)

    """Valid Sequence Problem"""
    # arrayIndex = 0
    # seqIndex = 0
    # while arrayIndex < len(array) and seqIndex < len(sequence):
    #     if array[arrayIndex] == sequence[seqIndex]:
    #         seqIndex += 1
    #     arrayIndex += 1
    # return seqIndex == len(sequence)
    star = '*'
    for i in range(10):
        print(star*i)

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def fournumbersum(array, targetSum):
    allPairSums = {}
    quadruplets = []
    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSums:
                for pair in allPairSums[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k], array[i]]]
            else:
                allPairSums[currentSum].append([array[k], array[i]])

    print(quadruplets)
    return quadruplets


def generateDocument(charactersGen, document):
    # Write your code here.
    characterCounts = {}

    for character in charactersGen:
        if character not in characterCounts:
            characterCounts[character] = 0

        characterCounts[character] += 1

    for character in document:
        if character not in characterCounts or characterCounts[character] == 0:
            return False

        characterCounts[character] -= 1

    return True


def bubble_sort(array):
    # Write your code here.
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                isSorted = False
        counter += 1
    return array


def getNthFib(n):
    # Write your code here.
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)


def insertionSort(array):
    # Write your code here.
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j -= 1

    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

    # Press the green button in the gutter to run the script.

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    smallest_diff = []
    current_diff = 0
    small_diff = 0
    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            current_diff = abs(arrayOne[i] - arrayTwo[j])
            if i == 0 and j == 0:
                small_diff = current_diff
                smallest_diff.append(arrayOne[i])
                smallest_diff.append(arrayTwo[j])
            elif current_diff < small_diff:
                small_diff = current_diff
                smallest_diff.remove(smallest_diff[0])
                smallest_diff.remove(smallest_diff[0])
                smallest_diff.append(arrayOne[i])
                smallest_diff.append(arrayTwo[j])
    return print(smallest_diff)


if __name__ == '__main__':
    # four = [7, 6, 4, -1, 1, 2]
    # target = 16
    n = 6
    array = [8, 5, 2, 9, 5, 6, 3]
    characterPass = "Bste!hetsi ogEAxpelrt x "
    name = "AlgoExpert is the Best!"
    arrayOne = [-1, 5, 10, 20, 28, 3]
    arrayTwo = [26, 134, 135, 15, 17]

    # print_hi('PyCharm')
    # smallestDifference(arrayOne, arrayTwo)
    # getNthFib(n)
    # fournumbersum(four, target)
    generateDocument(characterPass, name)
    # insertionSort(array)
    # bubble_sort(array)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""So, again, good night.

I must be cruel only to be kind.

This bad begins, and worse remains behind."""