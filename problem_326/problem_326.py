from basic import Node


def construct_cartesian_tree(inorder, start, end):
    if start > end:
        return None

    index = min_element_index(inorder, start, end)

    root = Node(inorder[index])
    root.left = construct_cartesian_tree(inorder, start, index - 1)
    root.right = construct_cartesian_tree(inorder, index + 1, end)

    return root


def min_element_index(inorder, start, end):
    min_index = start
    for i in range(start + 1, end + 1):
        if inorder[min_index] > inorder[i]:
            min_index = i

    return min_index
