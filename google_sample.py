import math
# def solution(array):
#     # Maximum k = |i - j| == |array[i] = array[j]|
#     # Difference between positions is equal to the difference between values
#     k = []
#     # first_map = {}
#     # second_map = {}
#     # for idx in range(len(array)):
#     #     # if abs(array[idx + 1] - array[idx]) == abs((idx + 1) - idx):
#     #     #     k.append(abs((idx+1)-idx))
#     #     # else:
#     #     first_map[idx - array[idx]] = idx
#     #     second_map[idx + array[idx]] = idx
#     #
#
#     # for num in array:
#     #     if
#
#     return 0


def solution(array):
    result = []
    if len(array) == 1:
        return print('0')
    for i in range(len(array)):
        for j in range(i, len(array)):
            if i == j:
                continue
            if abs(i - j) == abs(array[i] - array[j]):
                result.append(abs(i-j))
    return print(max(result))


if __name__ == '__main__':
    sample_array = [2, 4, 6, 7, 4, 7, 2]
    solution(sample_array)
    