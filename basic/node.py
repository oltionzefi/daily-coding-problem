class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder_traversal(node):
    if not node:
        return

    inorder_traversal(node.left)
    print(node.data, end=" ")
    inorder_traversal(node.right)
