import unittest
from problem_327 import MergeTree, TreeNode, readable_data
import io
from contextlib import redirect_stdout


class Problem327TestCase(unittest.TestCase):
    first_tree = TreeNode(1)
    first_tree.left = TreeNode(2)
    first_tree.right = TreeNode(3)
    first_tree.left.left = TreeNode(4)
    first_tree.left.right = TreeNode(5)
    first_tree.right.right = TreeNode(6)

    second_tree = TreeNode(4)
    second_tree.left = TreeNode(1)
    second_tree.right = TreeNode(7)
    second_tree.left.left = TreeNode(3)
    second_tree.right.left = TreeNode(2)
    second_tree.right.right = TreeNode(6)

    def test_merge_binary_tree(self):
        tree = MergeTree()
        merge_tree = tree.merge(self.first_tree, self.second_tree)

        f = io.StringIO()
        with redirect_stdout(f):
            readable_data(merge_tree)
        out = f.getvalue()

        self.assertIn("7 3 5 5 2 10 12", " ".join([x for x in out.split(" ")]))


if __name__ == "__main__":
    unittest.main()
