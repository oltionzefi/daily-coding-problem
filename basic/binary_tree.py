# simple implementation


class BinaryTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_node_value(self, value):
        self.value = value

    def get_node_value(self):
        return self.value

    def insert_right(self, new_node):
        if self.right is None:
            self.right = BinaryTree(new_node)
        else:
            tree = BinaryTree(new_node)
            tree.right = self.right
            self.right = tree

    def insert_left(self, new_node):
        if self.left is None:
            self.left = BinaryTree(new_node)
        else:
            tree = BinaryTree(new_node)
            tree.left = self.left
            self.left = tree
