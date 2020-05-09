import unittest
from problem_18 import max_sub_arrays, max_sub_arrays_deque


class Problem18TestCase(unittest.TestCase):
    list1 = [10, 5, 2, 7, 8, 7]
    k = 3

    def test_max_sub_arrays(self):
        self.assertEqual([10, 7, 8, 8], max_sub_arrays(self.list1, self.k))

    def test_max_sub_arrays_deque(self):
        self.assertEqual([10, 7, 8, 8], max_sub_arrays_deque(self.list1, self.k))


if __name__ == "__main__":
    unittest.main()
