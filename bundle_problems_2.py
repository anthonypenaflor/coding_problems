# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def classPhotos(redShirtHeights, blueShirtHeights):
    # Sort the arrays
    redShirtHeights.sort()
    blueShirtHeights.sort()
    bool_ = True

    # array_size_helper(redShirtHeights, blueShirtHeights)

    greatest_array = []
    smallest_array = []
    if blueShirtHeights[0] < redShirtHeights[0]:
        greatest_array = redShirtHeights
        smallest_array = blueShirtHeights
    elif blueShirtHeights[0] > redShirtHeights[0]:
        greatest_array = blueShirtHeights
        smallest_array = redShirtHeights
    else:
        bool_ = False
        return bool_
    # Determine back row
    for i in range(len(blueShirtHeights)):
        if greatest_array[i] < smallest_array[i]:
            bool_ = False
        else:
            bool_ = True

    return print(bool_)


def array_size_helper(blueShirtHeights, redShirtHeights):
    greatest_array = []
    smallest_array = []
    if blueShirtHeights < redShirtHeights:
        greatest_array = redShirtHeights
        smallest_array = blueShirtHeights
    else:
        greatest_array = blueShirtHeights
        smallest_array = redShirtHeights

    return greatest_array, smallest_array

def productSum(array, multiplier=1):
    # Write your code here.
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier


def tandem_bicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    total_sum = 0
    if not fastest:
        reverse_array(redShirtSpeeds)

    for i in range(len(redShirtSpeeds)):
        red_rider = redShirtSpeeds[i]
        blue_rider = blueShirtSpeeds[len(blueShirtSpeeds) - i - 1]
        total_sum += max(red_rider, blue_rider)

    return total_sum


def reverse_array(array):
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    current_node = linkedList
    while current_node is not None:
        next_distinct_node = current_node.next
        while next_distinct_node is not None and next_distinct_node.value == current_node.value:
            next_distinct_node = next_distinct_node.next

        current_node.next = next_distinct_node
        current_node = next_distinct_node

    return linkedList


def findThreeLargestNumbers(array):
    # Write your code here.
    three_num = [array[0], array[1], array[2]]
    sort_three(three_num)

    if len(array) > 3:
        for i in range(3, len(array)):
            if array[i] > three_num[0]:
                replace_num(three_num, array[i])

    return three_num


def sort_three(three_array):
    if three_array[1] > three_array[2]:
        three_array[1], three_array[2] = three_array[2], three_array[1]
    if three_array[0] > three_array[1]:
        three_array[0], three_array[1] = three_array[1], three_array[0]
    if three_array[1] > three_array[2]:
        three_array[1], three_array[2] = three_array[2], three_array[1]


def replace_num(current_array, replacement):
    count = 2
    while count >= 0:
        if replacement > current_array[count]:
            current_array[1], current_array[0] = current_array[2], current_array[0]
            current_array[count] = replacement
            break
        count -= 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')

    # Variables
    red_shirt = [5, 5, 3, 9, 2]
    blue_shirt = [3, 6, 7, 2, 1]
    array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    bool_ = True
    # blue = [5, 8, 1, 3, 4, 9]
    # red = [6, 9, 2, 4, 5, 1]
    three_nums = [3, 2, 1, 4, 10, -1, 42, 10]  # max three are: 10, 10, 42

    # Functions
    # classPhotos(red_shirt, blue_shirt)
    # productSum(array, multiplier=1)
    # tandem_bicycle(red_shirt, blue_shirt, bool_)
    findThreeLargestNumbers(three_nums)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
