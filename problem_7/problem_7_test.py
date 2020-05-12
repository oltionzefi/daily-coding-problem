import unittest
from problem_7 import way_of_decoding, ways_of_decoding_mem


class Problem7TestCase(unittest.TestCase):
    string = "111"

    def test_way_of_decoding(self):
        self.assertEqual(3, way_of_decoding(self.string))

    def test_ways_of_decoding_mem(self):
        self.assertEqual(3, ways_of_decoding_mem(self.string))


if __name__ == "__main__":
    unittest.main()
