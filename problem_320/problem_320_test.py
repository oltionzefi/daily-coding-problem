import unittest
from problem_320 import smallest_window, smallest_window_sw


class Problem320TestCase(unittest.TestCase):
    string = "jiujitsu"

    def test_smallest_window(self):
        self.assertEqual(5, smallest_window(self.string))

    def test_smallest_window_sw(self):
        self.assertEqual(5, smallest_window_sw(self.string))


if __name__ == "__main__":
    unittest.main()
