def merge(first_tree, second_tree):
    if not first_tree:
        return second_tree

    if not second_tree:
        return first_tree

    first_tree.data += second_tree.data
    first_tree.left = merge(first_tree.left, second_tree.left)
    first_tree.right = merge(first_tree.right, second_tree.right)

    return first_tree
