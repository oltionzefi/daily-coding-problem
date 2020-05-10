import unittest
from problem_20 import intersection_node


class Problem20TestCase(unittest.TestCase):
    list1 = [3, 7, 8, 10]
    list2 = [99, 1, 8, 10]

    list3 = [4, 5, 6, 1, 10, 4, 5, 6]
    list4 = [7, 1, 9, 3, 2, 11]

    def test_intersection_node_1(self):
        self.assertEqual(8, intersection_node(self.list1, self.list2))

    def test_intersection_node_2(self):
        self.assertEqual(1, intersection_node(self.list3, self.list4))


if __name__ == "__main__":
    unittest.main()
