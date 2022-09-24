def is_monotonic(array):
    non_decreasing = True
    non_increasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            non_decreasing = False
        if array[i] > array[i - 1]:
            non_increasing = False

    return non_increasing or non_decreasing


if __name__ == '__main__':
    """You're given an array of integers and an integer. Write a function that moves all instances of that integer in 
    the array to the end of the array and returns the array.
    The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain 
    the order of the other integers."""

    sample_array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
    is_monotonic(sample_array)
