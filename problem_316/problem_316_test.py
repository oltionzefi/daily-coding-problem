import unittest
from problem_316 import denominations


class Problem316TestCase(unittest.TestCase):
    list1 = [1, 0, 1, 1, 2]
    list2 = [1, 0, 1, 1, 2, 1]

    # def test_denominations(self):
    #     self.assertEqual("2, 3, 4", denominations(self.list1))

    def test_denominations_1(self):
        self.assertEqual("2, 3, 4", denominations(self.list2))


if __name__ == "__main__":
    unittest.main()
