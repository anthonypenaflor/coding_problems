def multiple_of_three_five(length):
    multiple_sum = 0
    for i in range(length):
        if i % 3 == 0 or i % 5 == 0:
            multiple_sum += i

    print(multiple_sum)
    return multiple_sum


def fibonacci(n):
    a = 0
    b = 1
    even_sum = 0

    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")

    # Check is n is equal
    # to 0
    elif n == 0:
        return 0

    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
            if b % 2 == 0:
                even_sum += b
                if even_sum > 4000000:
                    print(even_sum)
                    break
        return b, print(b), print(even_sum)

    # Driver Program
    # print(fibonacci(9))


def unique_characters(string):
    # Run through the array and catch i to search through the rest of the string for it's like value
    if len(string) > 128:
        return False
    char_set = [False for _ in range(128)]
    for i in string:
        val = ord(i)
        if char_set[val]:
            return False
        char_set[val] = True
    return True


def ways_to_make_change(n, denoms):
    ways = [0 for amount in range(n + 1)]
    ways[0] = 1

    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]


def threeNumberSort(array, order):
    for num in order:
        if num not in array:
            continue
        else:
            swap(array, array.index(num), order.index(num))

    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    return array


if __name__ == '__main__':
    # Variables for functions
    # multiple_length = 1000
    # n = 100
    # characters = "asdfjkl;"
    denoms = [1, 5, 10, 25]
    n = 6
    array = [1, 0, 0, -1, -1, 0, 1, 1]
    order = [0, 1, -1]

    # Functions
    # fibonacci(n)
    # unique_characters(characters)
    # ways_to_make_change(n, denoms)
    threeNumberSort(array, order)




