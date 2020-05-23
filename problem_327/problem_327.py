class MergeTree:
    def merge(self, first_tree, second_tree):
        if not first_tree:
            return second_tree

        if not second_tree:
            return first_tree

        first_tree.data += second_tree.data
        first_tree.left = self.merge(first_tree.left, second_tree.left)
        first_tree.right = self.merge(first_tree.right, second_tree.right)

        return first_tree


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def readable_data(node):
    if not node:
        return

    readable_data(node.left)
    print(node.data, end=" ")
    readable_data(node.right)
