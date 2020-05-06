import unittest
from problem_15 import pick


class Problem15TestCase(unittest.TestCase):
    stream = [[i, i] for i in range(1000)]

    def test_pick(self):
        self.assertIn(pick(self.stream), self.stream)


if __name__ == "__main__":
    unittest.main()
