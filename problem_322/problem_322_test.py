import unittest
from problem_322 import path_steps


class Problem322TestCase(unittest.TestCase):
    number_1 = 10
    number_2 = 11
    start = 0
    step = 0

    def test_path_steps_1(self):
        self.assertEqual(4, path_steps(self.start, self.step, self.number_1))

    def test_path_steps_2(self):
        self.assertEqual(5, path_steps(self.start, self.step, self.number_2))


if __name__ == "__main__":
    unittest.main()
