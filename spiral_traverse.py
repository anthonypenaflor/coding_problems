def spiral_traverse(array):
    # Write your code here.
    result = []
    spiral_fill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
    return result


def spiral_fill(array, start_row, end_row, start_col, end_col, result):
    if start_row > end_row or start_col > end_col:
        return

    for col in range(start_col, end_col + 1):
        result.append(array[start_row][col])

    for row in range(start_row + 1, end_row + 1):
        result.append(array[row][end_col])

    for col in reversed(range(start_col, end_col)):
        # Handle the edge case when there's a single row in the middle of the matrix
        if start_row == end_row:
            break
        result.append(array[end_row][col])

    for row in reversed(range(start_row + 1, end_row)):
        # Handle the edge case when there's a single column in the middle of the matrix
        if start_col == end_col:
            break
        result.append(array[row][start_col])

    spiral_fill(array, start_row + 1, end_row - 1, start_col + 1, end_col - 1, result)


if __name__ == '__main__':
    test_case = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]
    ]
    spiral_traverse(test_case)
