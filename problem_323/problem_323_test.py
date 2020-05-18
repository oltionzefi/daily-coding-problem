import unittest
from problem_323 import pick_pivot


class Problem323TestCase(unittest.TestCase):
    list1 = [1, 3, 4, 6, 2, 7, 9, 11, 12, 45, 34, 15]

    def test_median(self):
        self.assertEqual(7, int(pick_pivot(self.list1)))


if __name__ == "__main__":
    unittest.main()
