import unittest
from problem_333 import knows, get_celebrity


class Problem333TestCase(unittest.TestCase):
    list_of_known = {
        'user1': {'user2', 'user3'},
        'user2': {},
        'user3': 'user1'
    }

    def test_get_celebrity(self):
        self.assertEqual('user2', get_celebrity(self.list_of_known))

    def test_knows(self):
        self.assertEqual(False, knows(self.list_of_known, 'user2', 'user1'))

    def test_knows1(self):
        self.assertEqual(True, knows(self.list_of_known, 'user3', 'user1'))


if __name__ == "__main__":
    unittest.main()
