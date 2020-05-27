import unittest
from problem_331 import flip_count


class Problem331TestCase(unittest.TestCase):
    string1 = 'xyxxxyxyy'
    first_char1 = 'x'
    second_char1 = 'y'

    string2 = 'aaabaabbaab'
    first_char2 = 'a'
    second_char2 = 'b'

    def test_flip_count_1(self):
        self.assertEqual(2, flip_count(self.string1, self.first_char1, self.second_char1))

    def test_flip_count_2(self):
        self.assertEqual(3, flip_count(self.string2, self.first_char2, self.second_char2))


if __name__ == "__main__":
    unittest.main()
