import unittest
from problem_5 import cons, car, cdr


class Problem5TestCase(unittest.TestCase):
    pair1 = cons(3, 4)
    pair2 = cons(6, 7)
    res_car_1 = car(pair1)
    res_cdr_1 = cdr(pair1)
    res_car_2 = car(pair2)
    res_cdr_2 = cdr(pair2)

    # def test_cons(self):
    #     self.assertEqual(cons(3, 4), self.pair1)

    def test_cdr_1(self):
        self.assertEqual(4, self.res_cdr_1)

    def test_cdr_2(self):
        self.assertEqual(7, self.res_cdr_2)

    def test_car_1(self):
        self.assertEqual(3, self.res_car_1)

    def test_car_2(self):
        self.assertEqual(6, self.res_car_2)


if __name__ == "__main__":
    unittest.main()
