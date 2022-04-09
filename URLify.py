def urlify(url, length):
    """Write a method to replace all spaces in a string with '%20'. You may assume that the string
    has sufficient space at the end to hold the additional characters, and that you are given the "true"
    length of the string."""

    new_index = len(url)
    count = 0
    for char in url:
        if char == ' ':
            count += 1
    for i in reversed(range(length)):
        if url[i] == ' ':
            # Replace spaces
            url[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            url[new_index - 1] = url[i]
            new_index -= 1

    return url, print(url)


if __name__ == '__main__':
    url_string = 'anthony is super awesome       '
    string_length = 24
    urlify(url_string, string_length)
