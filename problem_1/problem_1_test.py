import unittest
from problem_1 import count_sets, count_sets_mem


class Problem1TestCase(unittest.TestCase):
    # Supposing that we have a list [3,4,5,8,9] and number 9
    set1 = [3, 4, 5, 8, 9]  # {9}, {4,5}
    number1 = 9

    def test_count_sets(self):
        self.assertEqual(count_sets(self.set1, self.number1), 2)

    def test_count_sets_mem(self):
        self.assertEqual(count_sets_mem(self.set1, self.number1), 2)


if __name__ == '__main__':
    unittest.main()
