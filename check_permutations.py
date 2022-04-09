from collections import Counter


def check_permutations(string1, string2):
    """Check if the two strings have identical character counts."""

    if len(string1) != len(string2):
        return False, print(False)

    counter = Counter()
    for char in string1:
        counter[char] += 1
    for char in string2:
        if counter[char] == 0:
            return False, print(False)

    return True, print(True)


if __name__ == '__main__':
    string_one = "airplane"
    string_two = "rialpnea"

    check_permutations(string_one, string_two)
