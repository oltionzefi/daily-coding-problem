import unittest
from problem_2 import prod_element, production, prod_element_rec, prod_element_rec_mem


class Problem2TestCase(unittest.TestCase):
    # Supposing that we have a list [1, 2, 3, 4, 5]
    # then result will be [120, 60, 40, 30, 24]
    set1 = [1, 2, 3, 4, 5]

    # Supposing that we have a list [3, 2, 1]
    # then result will be [2, 3, 6]
    set2 = [3, 2, 1]

    def test_prod_element_1(self):
        self.assertEqual([120, 60, 40, 30, 24], prod_element(self.set1))

    def test_prod_element_2(self):
        self.assertEqual([2, 3, 6], prod_element(self.set2))

    def test_production_key_0(self):
        self.assertEqual(120, production(self.set1, 0))

    def test_production_key_1(self):
        self.assertEqual(60, production(self.set1, 1))

    def test_prod_element_rec_1(self):
        self.assertEqual([120, 60, 40, 30, 24], prod_element_rec(self.set1))

    def test_prod_element_rec_2(self):
        self.assertEqual([2, 3, 6], prod_element_rec(self.set2))

    def test_prod_element_rec_mem_1(self):
        self.assertEqual([120, 60, 40, 30, 24], prod_element_rec_mem(self.set1))

    def test_prod_element_rec_mem_2(self):
        self.assertEqual([2, 3, 6], prod_element_rec_mem(self.set2))


if __name__ == '__main__':
    unittest.main()
