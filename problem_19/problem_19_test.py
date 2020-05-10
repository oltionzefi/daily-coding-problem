import unittest
from problem_19 import min_cost, min_cost_bu


class Problem19TestCase(unittest.TestCase):
    cost = [
        [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]
    ]
    m = 2
    n = 2

    def test_min_cost(self):
        self.assertEqual(8, min_cost(self.cost, self.m, self.n))

    def test_min_cost_bu(self):
        self.assertEqual(8, min_cost_bu(self.cost, self.m, self.n))


if __name__ == "__main__":
    unittest.main()
