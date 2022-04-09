class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    previousNode, currentNode = None, head

    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode

    return previousNode

first_node = LinkedList("a")
LinkedList.head = first_node
second_node = LinkedList("b")
third_node = LinkedList("c")
first_node.next = second_node
second_node.next = third_node
reverseLinkedList(first_node)