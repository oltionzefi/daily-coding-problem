import unittest
from problem_21 import rooms, rooms_sorted


class Problem21TestCase(unittest.TestCase):
    intervals = [(30, 75), (0, 50), (60, 150)]

    def test_rooms(self):
        self.assertEqual(2, rooms(self.intervals))

    def test_rooms_sorted(self):
        self.assertEqual(2, rooms_sorted(self.intervals))


if __name__ == "__main__":
    unittest.main()
