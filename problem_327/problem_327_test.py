import unittest
import io
from contextlib import redirect_stdout
from basic import Node, inorder_traversal
from problem_327 import merge


class Problem327TestCase(unittest.TestCase):
    first_tree = Node(1)
    first_tree.left = Node(2)
    first_tree.right = Node(3)
    first_tree.left.left = Node(4)
    first_tree.left.right = Node(5)
    first_tree.right.right = Node(6)

    second_tree = Node(4)
    second_tree.left = Node(1)
    second_tree.right = Node(7)
    second_tree.left.left = Node(3)
    second_tree.right.left = Node(2)
    second_tree.right.right = Node(6)

    def test_merge_binary_tree(self):
        merge_tree = merge(self.first_tree, self.second_tree)

        f = io.StringIO()
        with redirect_stdout(f):
            inorder_traversal(merge_tree)
        out = f.getvalue()

        self.assertIn("7 3 5 5 2 10 12", " ".join([x for x in out.split(" ")]))


if __name__ == "__main__":
    unittest.main()
