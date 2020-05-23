import unittest
from problem_328 import elo_rating


class Problem328TestCase(unittest.TestCase):
    k_upper = 32
    k_lower = 16
    rating_1 = 2000
    rating_2 = 1200
    rating_3 = 1300

    rating_point_advantage = 400

    def test_elo_rating_1(self):
        new_rating_a, new_rating_b = elo_rating(
            self.rating_1,
            self.rating_2,
            self.rating_point_advantage,
            self.k_upper,
            self.k_lower,
            winner='first'
        )

        self.assertEqual(2000.16, round(new_rating_a, 2))
        self.assertEqual(1199.84, round(new_rating_b, 2))

    def test_elo_rating_2(self):
        new_rating_a, new_rating_b = elo_rating(
            self.rating_1,
            self.rating_2,
            self.rating_point_advantage,
            self.k_upper,
            self.k_lower,
            winner='second'
        )

        self.assertEqual(1968.32, round(new_rating_a, 2))
        self.assertEqual(1231.68, round(new_rating_b, 2))

    def test_elo_rating_3(self):
        new_rating_a, new_rating_b = elo_rating(
            self.rating_1,
            self.rating_2,
            self.rating_point_advantage,
            self.k_upper,
            self.k_lower,
            winner='draw'
        )

        self.assertEqual(1992.16, round(new_rating_a, 2))
        self.assertEqual(1215.68, round(new_rating_b, 2))

    def test_elo_rating_4(self):
        new_rating_a, new_rating_b = elo_rating(
            self.rating_2,
            self.rating_3,
            self.rating_point_advantage,
            self.k_upper,
            self.k_lower,
            winner='first'
        )

        self.assertEqual(1220.48, round(new_rating_a, 2))
        self.assertEqual(1279.52, round(new_rating_b, 2))

    def test_elo_rating_5(self):
        new_rating_a, new_rating_b = elo_rating(
            self.rating_2,
            self.rating_3,
            self.rating_point_advantage,
            self.k_upper,
            self.k_lower,
            winner='second'
        )

        self.assertEqual(1194.24, round(new_rating_a, 2))
        self.assertEqual(1305.76, round(new_rating_b, 2))

    def test_elo_rating_6(self):
        new_rating_a, new_rating_b = elo_rating(
            self.rating_2,
            self.rating_3,
            self.rating_point_advantage,
            self.k_upper,
            self.k_lower,
            winner='draw'
        )

        self.assertEqual(1204.48, round(new_rating_a, 2))
        self.assertEqual(1297.76, round(new_rating_b, 2))


if __name__ == "__main__":
    unittest.main()
