import unittest
from problem_4 import lowest_value


class Problem4TestCase(unittest.TestCase):
    set1 = [3, 4, -1, 1]
    set2 = [1, 2, 0]
    set3 = [1, 2, 0, 5]
    set4 = [1, 2, 3, 4, 5]

    def test_lowest_value_1(self):
        self.assertEqual(2, lowest_value(self.set1))

    def test_lowest_value_2(self):
        self.assertEqual(3, lowest_value(self.set2))

    def test_lowest_value_3(self):
        self.assertEqual(3, lowest_value(self.set3))

    def test_lowest_value_4(self):
        self.assertEqual(6, lowest_value(self.set4))

    def test_lowest_value_insertion_sort_1(self):
        self.assertEqual(2, lowest_value(self.set1, 2))

    def test_lowest_value_insertion_sort_2(self):
        self.assertEqual(3, lowest_value(self.set2, 2))


if __name__ == '__main__':
    unittest.main()
