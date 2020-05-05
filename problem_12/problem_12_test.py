import unittest
from problem_12 import unique_ways, unique_ways_bu, unique_ways_with_conditions, unique_ways_with_conditions_bu


class Problem12TestCase(unittest.TestCase):
    n_1 = 4
    n_2 = 5
    x_1 = [1, 3, 5]
    x_2 = [1, 4]

    def test_unique_ways_1(self):
        self.assertEqual(5, unique_ways(self.n_1))

    def test_unique_ways_2(self):
        self.assertEqual(8, unique_ways(self.n_2))

    def test_unique_ways_bu_1(self):
        self.assertEqual(5, unique_ways(self.n_1))

    def test_unique_ways_bu_2(self):
        self.assertEqual(8, unique_ways_bu(self.n_2))

    def test_unique_ways_with_conditions_1(self):
        self.assertEqual(3, unique_ways_with_conditions(self.n_1, self.x_1))

    def test_unique_ways_with_conditions_2(self):
        self.assertEqual(3, unique_ways_with_conditions(self.n_2, self.x_2))

    def test_unique_ways_with_conditions_bu_1(self):
        self.assertEqual(3, unique_ways_with_conditions_bu(self.n_1, self.x_1))

    def test_unique_ways_with_conditions_bu_2(self):
        self.assertEqual(3, unique_ways_with_conditions_bu(self.n_2, self.x_2))


if __name__ == "__main__":
    unittest.main()
