import unittest
from problem_8 import count_unival_subtrees, cnt_unival_subtrees
from basic import BinaryTree


class Problem8TestCase(unittest.TestCase):
    #   a
    #  / \
    # a   a
    #     /\
    #    a  a
    #        \
    #         A
    # This tree has 3 unival subtrees
    leaf1_1 = BinaryTree('a')
    leaf1_1.insert_right('A')

    leaf1_2 = BinaryTree('a')
    leaf1_2.insert_left('a')
    leaf1_2.insert_right(leaf1_1)

    root_1 = BinaryTree('a')
    root_1.insert_left('a')
    root_1.insert_right(leaf1_2)

    #   a
    #  / \
    # c   b
    #     /\
    #    b  b
    #         \
    #          b
    # This tree has 5 unival subtrees: the leaf at ‘c’, and every ‘b’.
    leaf2_1 = BinaryTree('b')
    leaf2_1.insert_right('b')

    leaf2_2 = BinaryTree('b')
    leaf2_2.insert_left('b')
    leaf2_2.insert_right(leaf2_2)

    root_2 = BinaryTree('a')
    root_2.insert_left('c')
    root_2.insert_right(leaf2_2)

    def test_count_unival_subtrees_root_1(self):
        count = count_unival_subtrees(self.root_1)
        self.assertEqual(3, count)

    def test_count_unival_subtrees_root_2(self):
        count = count_unival_subtrees(self.root_2)
        self.assertEqual(5, count)

    def test_cnt_unival_subtrees_root_1(self):
        count = cnt_unival_subtrees(self.root_1)
        self.assertEqual(3, count)

    def test_cnt_unival_subtrees_root_2(self):
        count = cnt_unival_subtrees(self.root_2)
        self.assertEqual(5, count)


if __name__ == "__main__":
    unittest.main()
