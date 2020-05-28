import unittest
from problem_329 import stable_marriage


class Problem329TestCase(unittest.TestCase):
    guy_preferences = {
        'andrew': ['caroline', 'abigail', 'betty'],
        'bill': ['caroline', 'betty', 'abigail'],
        'chester': ['betty', 'caroline', 'abigail'],
    }

    gal_preferences = {
        'abigail': ['andrew', 'bill', 'chester'],
        'betty': ['bill', 'andrew', 'chester'],
        'caroline': ['bill', 'chester', 'andrew']
    }

    def test_stable_marriage(self):
        self.assertEqual(
            [('bill', 'caroline'), ('andrew', 'abigail'), ('chester', 'betty')],
            stable_marriage(self.guy_preferences, self.gal_preferences)
        )


if __name__ == "__main__":
    unittest.main()
