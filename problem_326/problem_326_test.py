import unittest
import io
from contextlib import redirect_stdout
from basic import inorder_traversal
from problem_326 import construct_cartesian_tree


class Problem326TestCase(unittest.TestCase):
    inorder_1 = [3, 2, 6, 1, 9]
    inorder_2 = [9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5]

    def test_construct_cartesian_tree_1(self):
        root_1 = construct_cartesian_tree(self.inorder_1, 0, len(self.inorder_1) - 1)

        f = io.StringIO()
        with redirect_stdout(f):
            inorder_traversal(root_1)
        out = f.getvalue()

        self.assertIn("3, 2, 6, 1, 9", ", ".join([x for x in out.split(" ")]))

    def test_construct_cartesian_tree_2(self):
        root_2 = construct_cartesian_tree(self.inorder_2, 0, len(self.inorder_2) - 1)

        f = io.StringIO()
        with redirect_stdout(f):
            inorder_traversal(root_2)
        out = f.getvalue()

        self.assertIn("9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5", ", ".join([x for x in out.split(" ")]))


if __name__ == "__main__":
    unittest.main()
