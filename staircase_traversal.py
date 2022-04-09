# O(n) time | O(n) space
def staircase_traversal(height, max_steps):
    current_number_of_ways = 0
    ways_to_top = [1]

    for current_height in range(1, height + 1):
        start_of_window = current_height - max_steps - 1
        end_of_window = current_height - 1
        if start_of_window >= 0:
            current_number_of_ways -= ways_to_top[start_of_window]

        current_number_of_ways += ways_to_top[end_of_window]
        ways_to_top.append(current_number_of_ways)

    return ways_to_top[height]


if __name__ == "__main__":
    ht = 4
    steps = 2
    staircase_traversal(ht, steps)
