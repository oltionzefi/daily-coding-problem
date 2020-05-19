import unittest
from problem_317 import bitwise_and, bitwise_and_with_lsb


class Problem317TestCase(unittest.TestCase):
    lower_limit_1 = 10
    upper_limit_1 = 15
    lower_limit_2 = 12
    upper_limit_2 = 15

    def test_bitwise_and_1(self):
        self.assertEqual(8, bitwise_and(self.lower_limit_1, self.upper_limit_1))

    def test_bitwise_and_2(self):
        self.assertEqual(12, bitwise_and(self.lower_limit_2, self.upper_limit_2))

    def test_bitwise_and_3(self):
        self.assertEqual(8, bitwise_and_with_lsb(self.lower_limit_1, self.upper_limit_1))

    def test_bitwise_and_4(self):
        self.assertEqual(12, bitwise_and_with_lsb(self.lower_limit_2, self.upper_limit_2))


if __name__ == "__main__":
    unittest.main()
