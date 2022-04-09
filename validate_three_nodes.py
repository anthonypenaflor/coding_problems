class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(h) time | O(h) space
def validate_three_nodes(node_one, node_two, node_three):
    # Write your code here.
    if is_descendant(node_two, node_one):
        return is_descendant(node_three, node_two)

    if is_descendant(node_two, node_three):
        return is_descendant(node_one, node_two)

    return False


# O(h) time | O(1) space
def is_descendant(node, target):
    while node is not None and node is not target:
        node = node.left if node.value > target.value else node.right

    return node is target


# When using recursion:
# O(h) time | O(h) space
# def is_descendant(node, target):
#     if node is None:
#         return False
#
#     if node is target:
#         return True
#
#     return is_descendant(node.left, target) if target.value < node.value else is_descendant(node.right, target)


if __name__ == '__main__':
    one = 5
    two = 2
    three = 3
    validate_three_nodes(one, two, three)
