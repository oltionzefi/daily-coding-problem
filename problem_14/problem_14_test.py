import unittest
from problem_14 import estimate_pi


class Problem14TestCase(unittest.TestCase):
    dp = 3

    # we can not do specific assertion since it is based on random generation
    def test_estimate_pi(self):
        self.assertGreaterEqual(estimate_pi(self.dp), 3.1)


if __name__ == "__main__":
    unittest.main()
