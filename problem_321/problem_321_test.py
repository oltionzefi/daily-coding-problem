import unittest
from problem_321 import smaller_number_steps


class Problem321TestCase(unittest.TestCase):
    N = 100

    def test_smaller_number_steps(self):
        self.assertEqual("100 -> 10 -> 5 -> 4 -> 2 -> 1", smaller_number_steps(self.N))


if __name__ == "__main__":
    unittest.main()
