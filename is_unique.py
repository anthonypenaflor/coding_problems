def unique_characters(string):
    """Implement an algorithm to determine if a string has all unique characters. What if you cannot use
    additional data structures?"""

    if len(string) > 128:
        return False
    char_set = [False for _ in range(128)]
    for i in string:
        val = ord(i)
        if char_set[val]:
            return False
        char_set[val] = True
    return True


if __name__ == '__main__':
    characters = "asd$%13"
    unique_characters(characters)
