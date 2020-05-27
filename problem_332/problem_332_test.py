import unittest
from problem_332 import positive_integer_pairs


class Problem332TestCase(unittest.TestCase):
    m = 100
    n = 4

    def test_positive_integer_pairs(self):
        results = positive_integer_pairs(self.m, self.n)
        self.assertEqual([(48, 52)], results)


if __name__ == "__main__":
    unittest.main()
