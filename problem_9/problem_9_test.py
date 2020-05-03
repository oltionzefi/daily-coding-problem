import unittest
from .problem_9 import find_max_sum


class Problem9TestCase(unittest.TestCase):
    list1 = [5, 1, 1, 5]
    list2 = [2, 4, 6, 2, 5]

    def test_find_max_sum_1(self):
        self.assertEqual(10, find_max_sum(self.list1))

    def test_find_max_sum_2(self):
        self.assertEqual(13, find_max_sum(self.list2))


if __name__ == "__main__":
    unittest.main()