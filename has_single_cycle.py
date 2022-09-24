# O(n) time | O(1) space
def has_single_cycle(array):
    # write here
    visited = 0
    current_idx = 0
    while visited < len(array):
        if visited > 0 and current_idx == 0:
            return False
        visited += 1
        current_idx = get_next_idx(current_idx, array)
    return current_idx == 0


def get_next_idx(current_idx, array):
    jump = array[current_idx]
    next_idx = (current_idx + jump) % len(array)
    return next_idx if next_idx >= 0 else next_idx + len(array)


if __name__ == '__main__':
    array_sample = [2, 3, 1, -4, -4, 2]
    has_single_cycle(array_sample)
