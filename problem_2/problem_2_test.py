import unittest
from problem_2 import prod_element, production


class Problem2TestCase(unittest.TestCase):
    # Supposing that we have a list [1, 2, 3, 4, 5]
    # then result will be [120, 60, 40, 30, 24]
    set1 = [1, 2, 3, 4, 5]

    # Supposing that we have a list [3, 2, 1]
    # then result will be [2, 3, 6]
    set2 = [3, 2, 1]

    def test_prod_element_1(self):
        self.assertEqual(prod_element(self.set1), [120, 60, 40, 30, 24])

    def test_prod_element_2(self):
        self.assertEqual(prod_element(self.set2), [2, 3, 6])

    def test_production_key_0(self):
        self.assertEqual(production(self.set1, 0), 120)

    def test_production_key_1(self):
        self.assertEqual(production(self.set1, 1), 60)


if __name__ == '__main__':
    unittest.main()
