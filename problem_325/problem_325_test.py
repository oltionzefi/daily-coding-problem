import unittest
from problem_325 import Graph


class Problem325TestCase(unittest.TestCase):
    g = Graph()
    g.add_edge("km", "m", 1000)
    g.add_edge("m", "cm", 100)

    g.dfs()

    def test_convert(self):
        pass


if __name__ == "__main__":
    unittest.main()
