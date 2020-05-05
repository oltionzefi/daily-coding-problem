import unittest
from problem_13 import longest_substr


class Problem13TestCase(unittest.TestCase):
    string = "abcba"
    k_1 = 2
    k_2 = 0
    k_3 = 6

    def test_longest_substr_1(self):
        self.assertEqual("bcb", longest_substr(self.string, self.k_1))

    def test_longest_substr_2(self):
        self.assertEqual(None, longest_substr(self.string, self.k_2))

    def test_longest_substr_3(self):
        self.assertEqual("abcba", longest_substr(self.string, self.k_3))


if __name__ == "__main__":
    unittest.main()
